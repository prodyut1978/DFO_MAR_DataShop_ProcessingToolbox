# DFO_MAR_DataShop_ProcessingToolbox
**Unclassified – Non Classifié**

---

## 🌊 Overview
The **DFO_MAR_DataShop_ProcessingToolbox** is a Python-based data processing and quality control (QC) toolbox developed by the **Ocean Data Management Group** at the **Bedford Institute of Oceanography (BIO)**, Fisheries and Oceans Canada (DFO).

This toolbox supports the processing, QC, and archival preparation of oceanographic data, including:

- Moored temperature (thermograph) data  
- CTD data from Sea-Bird instruments  

### 🎯 Objective
The primary goal is to convert raw and semi-processed instrument data into **DFO’s Ocean Data Format (ODF)** while enforcing **robust and reproducible QC workflows**.

---

## 👨‍🔬 Authors
- **Jeff Jackson**, Fisheries and Oceans Canada (DFO)  
- **Prodyut Kumar Roy**, Fisheries and Oceans Canada (DFO)  

Developed and maintained by the **Ocean Data Group**,  
Bedford Institute of Oceanography (BIO)

---

## ⚙️ Installation

### 1️⃣ Requirements
- Python ≥ 3.10  
- NumPy  
- Pandas  
- Matplotlib  
- PySide6 (for GUI QC tools)
- scipy
- netCDF4
- gsw

---

### 2️⃣ Setup
#### Step 1: Create environment
uv venv
#### Step 2: Activate environment
.venv\Scripts\activate
#### Step 3: Install dependencies
uv sync


▶️ Run Toolbox 

- To process and QC MTR (Moored Temp Record) data
   ## Run MTR tools

   uv run run_MTR_tools.py

   or

   uv run python -m run_MTR_tools

## 📁 Package Structure
DFO_MAR_DataShop_ProcessingToolbox/
├── src/
│ ├── datashop_toolbox/
│ │ ├── headers/ # ODF header classes
│ │ ├── thermograph.py # Thermograph processing core
│ │ ├── qc_thermograph_data.py # QC for thermograph data
│ │ └── process_mtr_files.py # MTR processing pipeline
│ │
│ ├── seabird/
│ │ ├── cnv.py # Sea-Bird CNV parser
│ │ └── cnv.json # CNV parsing rules
│ │
│ ├── CoTeDe/
│ │ └── qc.py # Custom QC tests
│
├── run_SEABIRD_tools.py # Example runner
├── run_MTR_tools.py # Example runner
├── README.md
└── ODF_File_Specification.md


## 🧩 Core Components

### 1️⃣ `datashop_toolbox` (DFO Proprietary)

Implements core processing using Python OOP principles:

- Reading raw MTR and CTD data  
- Structured metadata handling  
- Quality flag assignment  
- Writing to **Ocean Data Format (ODF)**  

📄 **ODF Specification (v3.0):**  
👉 https://github.com/jeff-jackson-dfo/datashop_toolbox/blob/master/ODF_File_Specification.md  

---

### 2️⃣ Sea-Bird CNV Parsing (`seabird`)

Extends the PySeabird parser for CNV files.

#### ✨ Features
- Supports multiple Sea-Bird firmware formats  
- Handles:
  - Commented XML / CDATA blocks  
  - Partial metadata (lat/lon, station, cast)  
- Stores data as NumPy masked arrays  
- Converts DMS → decimal degrees automatically  

#### 💡 Example
```python
from seabird.cnv import fCNV

profile = fCNV("input_file.CNV")

# Defensive defaults (recommended)
profile.attrs.setdefault("LATITUDE", "")
profile.attrs.setdefault("LONGITUDE", "")

df = profile.as_DataFrame()