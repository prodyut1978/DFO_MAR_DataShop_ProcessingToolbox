import seabird
from seabird.cnv import fCNV
from seabird.qc import fProfileQC




cnv_file_location = "./sampledata/cnv/D900a108.cnv"
profile = fCNV(cnv_file_location)



df = profile.as_DataFrame()
print(df.head())