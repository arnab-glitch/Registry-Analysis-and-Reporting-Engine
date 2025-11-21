# Workflow — How RegEx-Analysis Works

RegEx-Analysis follows a simple 3-stage pipeline:

---

## 1. Input Stage
The tool reads all evidence from the selected folder inside `/evidence/`:

- manifest.json  
- usb_history.csv  
- regex_log.txt  
- Prefetch + Event Logs (metadata only)

It also loads the HTML template + CSS theme from `/templates/`.

---

## 2. Processing Stage
The script performs:
- Validation of manifest format
- Count & classification of evidence items
- Extraction of key metadata (hashes, paths, status)
- Building USB device list
- Summary generation:
  - Total items
  - Acquisition mode
  - Operator
  - Manifest hash
  - Evidence health
- Formatting of log output

---

## 3. Rendering Stage
Using Jinja2:
- Data is injected into `report_template.html`
- Status badges (OK/FAIL) are applied
- CSS theme is linked
- Tabs: Overview, USB, Evidence, Logs
- File saved to: /output/RegEx_Report.html

The HTML report can be viewed in any browser.

---

## Notes
- The workflow is fully offline  
- No external dependencies besides Python/Jinja2  
- Output is static HTML (no server required)  

