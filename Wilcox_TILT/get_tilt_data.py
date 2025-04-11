import os
import time
import pickle
import pandas as pd
from bs4 import BeautifulSoup
from import2 import simple_get
from DECIMAL import decimal_year

# --- Config ---
base_dir = "/var/www/ricco_website/HVO_CRISP/Wilcox_TILT/data"
text_path = os.path.join(base_dir, "tilt.txt")

# --- Fetch and parse HTML ---
response = simple_get("http://wso.stanford.edu/Tilts.html")
soup = BeautifulSoup(response, "html.parser")

# --- Save raw <pre> data to tilt.txt ---
with open(text_path, "w") as f:
    for pre in soup.select("pre"):
        f.write(pre.text)

# --- Read and clean lines ---
with open(text_path, "r") as f:
    lines = f.readlines()

# Remove first two header lines
data_lines = lines[2:]

# --- Process and collect data ---
tilt_data = []
for line in data_lines:
    sline = line.strip().split()
    if len(sline) < 10:
        continue  # skip malformed lines

    try:
        year = int(sline[2][0:4])
        month = int(sline[2][5:7])
        day = int(sline[2][8:10])
        date = decimal_year(year, month, day)

        tilt_data.append(
            {
                "decimal_year": date,
                "R_av": float(sline[4]),
                "R_n": float(sline[5]),
                "R_s": float(sline[6]),
                "L_av": float(sline[7]),
                "L_n": float(sline[8]),
                "L_s": float(sline[9]),
            }
        )
    except Exception as e:
        print(f"Skipping line due to error: {e}")
        continue

# --- Save as multiple .txt files and a .pkl ---
df = pd.DataFrame(tilt_data)

# Save each column as its own .pkl file (with decimal_year included)
for col in df.columns[1:]:  # skip 'decimal_year' only
    col_df = df[["decimal_year", col]].copy()
    out_path = os.path.join(base_dir, f"Tilt_{col}.pkl")

    with open(out_path, "wb") as f:
        pickle.dump(col_df, f)
