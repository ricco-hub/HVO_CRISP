import os
import re
import pickle
import sys
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime
from import2 import simple_get

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.utils import timestamp_to_decimal_year


# --- Config ---
base_dir = "/var/www/ricco_website/HVO_CRISP/Wilcox_SFS/data"
text_path = os.path.join(base_dir, "polar.txt")

# --- Fetch and save raw HTML ---
response = simple_get("http://wso.stanford.edu/Polar.html")
soup = BeautifulSoup(response, "html.parser")

with open(text_path, "w") as f:
    for pre in soup.select("pre"):
        f.write(pre.text)

# --- Read lines ---
with open(text_path, "r") as f:
    lines = f.readlines()

# Remove first two header lines if necessary
data_lines = lines[2:] if len(lines) > 2 else lines

# --- Regex to extract fields ---
pattern = re.compile(
    r"(?P<timestamp>\d{4}:\d{2}:\d{2}_\d{2}h:\d{2}m:\d{2}s)\s+"
    r"(?P<N>-?\d+)N\s+(?P<S>-?\d+)S\s+(?P<A>-?\d+)Avg\s+20nhz filt:\s+"
    r"(?P<Nf>-?\d+)Nf\s+(?P<Sf>-?\d+)Sf\s+(?P<Af>-?\d+)Avgf"
)

# --- Process data ---
polar_data = []
for line in data_lines:
    match = pattern.search(line)
    if not match:
        continue  # Skip malformed lines

    try:
        timestamp = match.group("timestamp")
        decimal = timestamp_to_decimal_year(timestamp)
        polar_data.append(
            {
                "decimal_year": decimal,
                "N": float(match.group("N")),
                "S": float(match.group("S")),
                "A": float(match.group("A")),
                "Nf": float(match.group("Nf")),
                "Sf": float(match.group("Sf")),
                "Af": float(match.group("Af")),
            }
        )
    except Exception as e:
        print(f"Skipping line due to error: {e}")
        continue

# --- Save results ---
df = pd.DataFrame(polar_data)

for col in df.columns[1:]:  # skip decimal_year
    col_df = df[["decimal_year", col]]
    out_path = os.path.join(base_dir, f"Polar_{col}.pkl")
    with open(out_path, "wb") as f:
        pickle.dump(col_df, f)
