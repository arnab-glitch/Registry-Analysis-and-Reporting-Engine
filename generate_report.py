#!/usr/bin/env python3

import csv
import json
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# ------------------ UNIVERSAL PATHS (PORTABLE) ------------------

# Base folder = the folder where generate_report.py is located
BASE_DIR = Path(__file__).resolve().parent

# Evidence folder (user places case folder here)
EVIDENCE_ROOT = BASE_DIR / "evidence"

# Auto-detect latest evidence folder (or fallback)
evidence_folders = [f for f in EVIDENCE_ROOT.iterdir() if f.is_dir()]
if evidence_folders:
    EVIDENCE_DIR = evidence_folders[0]   # first folder inside /evidence/
else:
    raise Exception("No evidence folder found in /evidence/. Please add one.")

# Templates directory (relative)
TEMPLATES_DIR = BASE_DIR / "templates"

# Output folder
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_HTML = OUTPUT_DIR / "RegEx_Report.html"

# Tool metadata
TOOL_NAME = "RegEx"
TOOL_VERSION = "1.0"
DEVELOPER = "Arnab Das"

# ---------------------------------------------------------

def safe_read(path):
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except:
        return ""

def load_manifest(path):
    if not path.exists():
        print("ERROR: manifest.json not found at:", path)
        return {}

    raw = path.read_bytes()

    # Remove UTF-8 BOM
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]

    try:
        return json.loads(raw.decode("utf-8"))
    except Exception as e:
        print("ERROR parsing manifest:", e)
        return {}

def load_usb(path):
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "timestamp": "",
                "device_id": r.get("instance", r.get("vendor_key", "")),
                "serial": r.get("parent", ""),
                "model": r.get("friendly", ""),
                "user": "",
                "action": "Connected"
            })
    return rows

def main():

    print("Using evidence folder:", EVIDENCE_DIR)

    manifest = load_manifest(EVIDENCE_DIR / "manifest.json")
    usb = load_usb(EVIDENCE_DIR / "usb_history.csv")
    log = safe_read(EVIDENCE_DIR / "regex_log.txt")

    items = manifest.get("items", [])
    case_id = manifest.get("case_id", EVIDENCE_DIR.name)
    operator = manifest.get("operator", "UNKNOWN")
    method = manifest.get("method", "UNKNOWN").upper()
    manifest_hash = manifest.get("manifest_hash", "")

    case = {
        "case_id": case_id,
        "operator": operator,
        "report_date": datetime.now().isoformat(),
        "total_files": len(items),
        "tool_version": f"{TOOL_NAME} v{TOOL_VERSION}",
        "developer": DEVELOPER,
        "quality": "Full Forensic Extraction",
        "manifest_hash": manifest_hash,
        "mode": method,
    }

    analysis = {
        "summary": (
            f"RegEx v1 performed a full {method}-mode forensic acquisition. "
        ),
        "findings": [
            f"{len(usb)} USB devices detected.",
            f"{len(items)} evidence items extracted.",
            f"Manifest hash: {manifest_hash}",
            f"Reported by {operator} using RegEx v1.0"
        ]
    }

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    tpl = env.get_template("report_template.html")

    # Add friendly fallback source label for empty source
    for it in items:
     src = it.get("source")
     if not src:
        art = it.get("artifact", "")
        it["source"] = f"{art} (registry export)" if it.get("method","").startswith("reg") else f"{art} (unknown source)"

    html = tpl.render(
     case=case,
     usb=usb,
     items=items,
     analysis=analysis,
     log_text=log
)

    # WRITE HTML INSTEAD OF PDF
    OUTPUT_HTML.write_text(html, encoding="utf-8")

    print("HTML Report generated successfully at:", OUTPUT_HTML)

if __name__ == "__main__":
    main()
