# RegEx-Analysis — Overview

RegEx-Analysis is the second half of the RegEx forensic workflow.

It processes evidence collected by **RegEx-Acquisition** and generates a
professional, interactive HTML forensic report. The goal is to automate
post-acquisition review, USB activity reconstruction, artifact validation,
and chain-of-custody documentation.

---

## What This Tool Does
- Loads manifest.json from RegEx-Acquisition
- Parses USB device history metadata
- Displays extraction status for each artifact
- Shows SHA256 integrity hashes
- Renders acquisition logs in a formatted viewer
- Generates a clean, neon-themed HTML report

---

## Who Is This Tool For?
- Forensic analysts  
- Incident responders  
- Students learning DFIR  
- Law enforcement digital forensics  
- Cyber investigation professionals  

---

## Supported Evidence Types
- Registry hive exports  
- Event logs  
- Prefetch metadata  
- USB device entries  
- Amcache (best-effort)  
- Acquisition logs  
- Manifest.json  
