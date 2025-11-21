<!-- ========================================= -->
<!--           REGEX ANALYSIS README           -->
<!-- ========================================= -->

<!-- CENTERED HEADER WITH LOGO -->
<p align="center">
  <img src="./templates/regex_logo.png" width="140" height="140" alt="RegEx Logo" style="border-radius: 12px;">
</p>

<h1 align="center" style="color:#00eaff; font-weight:700; font-size:42px;">
  RegEx Analysis & Reporting Engine (v1.0)
</h1>

<p align="center" style="font-size:17px; color:#b5b5b5;">
  <b>Python-Based DFIR Report Generator • Neon Forensic UI Theme • Built by Arnab Das</b>
</p>

<br>

<!-- BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-00eaff?style=for-the-badge&logo=windows-terminal">
  <img src="https://img.shields.io/badge/Language-Python_3.8+-ffdd00?style=for-the-badge&logo=python&logoColor=000">
  <img src="https://img.shields.io/badge/Rendering-Jinja2-ff4df0?style=for-the-badge&logo=jinja">
  <img src="https://img.shields.io/badge/Report-HTML%20Interactive-00ff95?style=for-the-badge&logo=html5">
  <img src="https://img.shields.io/badge/Part_of-RegEx%20Forensic%20Suite-ff2a2a?style=for-the-badge">
</p>

<br><br>

## 🔗 Related Project

Need the acquisition tool to collect Windows registry artifacts?

[![Related Tool](https://img.shields.io/badge/Portable%20Registry%20Acquisition%20Tool-ff4df0?style=for-the-badge)](https://github.com/arnab-glitch/Portable-Registry-Acquisition-Tool)

This is the companion evidence collection tool required before running the analysis engine.

---

<!-- INTRO SECTION -->
<h2 style="color:#00eaff;">🔍 Overview</h2>

RegEx-Analysis is the companion project to the **RegEx Portable Registry Acquisition Tool**.  
This engine takes the collected forensic artifacts, parses the metadata, and automatically generates an **interactive neon-themed HTML forensic report**.

✔ No installation required  
✔ Works on any PC (Windows, Linux, macOS)  
✔ Uses only Python + Jinja2  
✔ Fully portable for DFIR workflows  

<br>

---

## 🧬 **Key Features**
<ul style="font-size:17px; line-height:1.6;">
  <li>🟦 Generates a full interactive <b>HTML forensic report</b> (dark neon theme)</li>
  <li>🟩 Parses <b>manifest.json, usb_history.csv, regex_log.txt</b></li>
  <li>🟣 Displays registry hives, hashes, artifacts, and extraction status</li>
  <li>🟧 USB device history reconstruction (USBSTOR metadata)</li>
  <li>🔵 Searchable + scrollable Evidence Table</li>
  <li>🔴 OK/FAIL status badges</li>
  <li>🟡 Automatic folder detection (no hard-coded paths)</li>
</ul>

<br>

---

## 📁 **Repository Structure**

```
RegEx-Analysis/
│
├── generate_report.py
├── README.md
├── LICENSE
│
├── templates/
│   ├── report_template.html
│   ├── report_style.css
│   └── regex_logo.png
│
│
├── evidence/
│   └── .gitignore
│
├── output/
│   └── RegEx_Report.html   (auto-generated)
│
└── docs/
    ├── overview.md
    ├── workflow.md
    └── requirements.md
    
    
```

<br>

---

## ⚙️ **Installation & Requirements**

### Install dependencies:
```bash
pip install jinja2
```

Or use:
```bash
pip install -r requirements.txt
```

### Requirements:
✔ Python 3.8+  
✔ Works offline  
✔ No admin rights needed  

<br>

---

## 🚀 **How to Use**

1. Place your RegEx evidence folder under:

```
RegEx-Analysis/evidence/XX-XXXX-001/
```

2. Run the report generator:

```bash
python generate_report.py
```

3. Your final interactive report is generated at:

```
RegEx-Analysis/output/RegEx_Report.html
```

4. Open the HTML file in any browser.

<br>

---

## 🎨 **HTML Report Features**
The report contains:

### 🟦 **Overview Tab**
- Case ID  
- Operator  
- Acquisition mode  
- Total evidence  
- Manifest hash  
- Key summary  

### 🟩 **USB Artifacts**
Lists:
- Device paths  
- Serial numbers  
- Models  
- Connection events  

### 🟨 **Evidence Table**
- Searchable filter  
- OK/FAIL badges  
- SHA256 hashes  
- Source categories  

### 🟥 **Log Output**
- Full acquisition logs  
- Time-stamped errors  
- VSS fallback notes  

<br>

---

## 🧪 **Example Output**


*See the `/output/` folder for sample reports.*



---

## 🧑‍💻 **Author**

**Arnab Das**  
Master’s Student — Cyber Forensics  
National Forensic Sciences University  

<br>

---

## 📄 **License**

This project is licensed under the **MIT License**.  
Feel free to fork, modify, and contribute.

<br>

---

<!-- FOOTER -->
<p align="center" style="color:#00eaff; font-size:16px; margin-top:30px;">
⚡ Part of the RegEx Forensic Analysis Suite • Built for DFIR • Made with ❤️ & Python ⚡
</p>

