DFO_MAR_DataShop_ProcessingToolbox
----------------------------------
Unclassified – Non Classifié
Overview
The DFO_MAR_DataShop_ProcessingToolbox is a Python based data processing and quality control toolbox developed by the Ocean Data Management Group at the Bedford Institute of Oceanography (BIO), Fisheries and Oceans Canada (DFO).
The toolbox supports the processing, quality control (QC), and archival preparation of oceanographic data, including:
•	Moored temperature (thermograph) data
•	CTD data originating from Sea Bird instruments
The primary goal of this toolbox is to convert raw and semi processed instrument data into DFO’s in house Ocean Data Format (ODF), while enforcing robust, reproducible QC workflows.
Authors
•	Jeff Jackson, Fisheries and Oceans Canada (DFO)
•	Prodyut Kumar Roy, Fisheries and Oceans Canada (DFO)
Developed and maintained by the Ocean Data Group,
Bedford Institute of Oceanography (BIO).


Installation
-------------
1: Requirements
Requirements
Python ≥ 3.10
NumPy, Pandas, Matplotlib
PySide6 (for GUI QC tools)

2. Setup
>> Step : 01 >> Create environment: 
uv venv

>> Step : 02 >> Activate environment: 
.venv\Scripts\activate

>> Step : 03 >> Install pyproject.toml file: 
uv sync

<<<<<<<<<<< To Run Datashop_Toolbox MTR Tools >>>>>>>
>>> uv run run_MTR_tools.py or uv run python -m run_MTR_tools



Package Structure
-------------------
DFO_MAR_DataShop_ProcessingToolbox/
├── src/
│   ├── datashop_toolbox/
│   │   ├── headers/              # ODF header classes
│   │   ├── thermograph.py        # Thermograph processing core
│   │   ├── qc_thermograph_data.py  # Run QC on Thermograph Data
│   │   └── process_mtr_files.py  # Run Processing on Thermograph Data
│   │
│   ├── seabird/
│   │   ├── cnv.py                # Sea Bird CNV parser
│   │   └── cnv.json              # CNV parsing rules
│
│   ├── CoTeDe/
│   │   ├── qc.py                # Custom user defined QC tests
├──  Build your own custom tools (e.g. run_SEABIRD_tools.py or run_MTR_tools.py)
├── README.md
└── ODF_File_Specification.md
________________________________________

Core Components:
----------------------

01: datashop_toolbox (DFO proprietary)
The datashop_toolbox package is written using Python OOP principles and implements:
•	Reading and processing of raw moored temperature (MTR) and CTD data
•	Metadata handling using structured header objects
•	Quality flag assignment
•	Writing of data to Ocean Data Format (ODF)
📄 ODF Specification
The current ODF format is Version 3.0:
➡️ https://github.com/jeff-jackson-dfo/datashop_toolbox/blob/master/ODF_File_Specification.md

________________________________________
02: Sea Bird CNV Parsing (seabird)
This toolbox includes and extends the PySeabird parser for Sea Bird CNV files.
Capabilities include:
•	Parsing CNV files across multiple Sea Bird firmware generations
•	Robust handling of: 
o	Commented XML / CDATA blocks
o	Partially filled metadata (latitude/longitude, station, cast)
•	Storage of data as NumPy masked arrays
•	Automatic conversion of DMS latitude/longitude to decimal degrees
Example usage:
Python
from seabird.cnv import fCNV
profile = fCNV("input_file.CNV")

# Defensive defaults (recommended)
profile.attrs.setdefault("LATITUDE", "")
profile.attrs.setdefault("LONGITUDE", "")
df = profile.as_DataFrame()
Show more lines
⚠️ Important note
The upstream Sea Bird parser assumes certain metadata fields (e.g., LATITUDE, LONGITUDE) always exist.
This toolbox enforces defensive defaults to avoid runtime failures.
________________________________________
03: Quality Control with CoTeDe
The toolbox integrates CoTeDe, an open source framework for oceanographic QC.
Key features of CoTeDe:
•	Predefined QC procedures following: 
o	GTSPP
o	QARTOD
o	Argo
o	XBT standards
•	Custom user defined QC tests
•	Fuzzy logic approaches
•	Anomaly detection using machine learning
Relevant references:
•	Castelão, G.P. (2020), Journal of Open Source Software
•	Castelão, G.P. (2021), Computers & Geosciences
📚 Documentation:
https://cotede.readthedocs.io
________________________________________
04: OceansDB (Climatological comparisons)
For secondary QC and validation, the toolbox can leverage OceansDB:
•	World Ocean Atlas (WOA)
•	CSIRO Atlas Regional Seas (CARS)
•	ETOPO topography
Example:
Python
import oceansdb
with oceansdb.WOA() as db:
temp = db["sea_water_temperature"].extract(
lat=45.0, lon=-60.0, depth=10, doy=150, var="mean"
)
Show more lines
Documentation:
https://oceansdb.readthedocs.io









