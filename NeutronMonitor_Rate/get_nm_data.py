import datetime
import os
import time
import pickle
import pandas as pd

from bs4 import BeautifulSoup
from import2 import simple_get
from DECIMAL import decimal_year
from import2 import simple_get  # Custom, retain if needed


def fetch_data(station, resolution):
    now = datetime.datetime.now()
    url = (
        f"http://www.nmdb.eu/nest/draw_graph.php?formchk=1&stations[]={station}"
        f"&tabchoice=1h&dtype=corr_for_efficiency&tresolution={resolution}"
        f"&yunits=0&date_choice=bydate&start_day=1&start_month=1&start_year=1960"
        f"&start_hour=0&start_min=0&end_day={now.day}&end_month={now.month}&end_year={now.year}"
        f"&end_hour=23&end_min=59&output=ascii"
    )
    response = simple_get(url)
    html = BeautifulSoup(response, "html.parser")
    pre_data = html.select("pre")[0].text.splitlines()

    data = []
    for line in pre_data[25:]:
        try:
            year = int(line[0:4])
            month = int(line[5:7])
            day = int(line[8:10])
            date_decimal = decimal_year(year, month, day)
            value = float(line.split()[2])
            data.append((date_decimal, value))
        except Exception as e:
            print("Parsing error:", e, line)

    df = pd.DataFrame(data, columns=["decimal_year", "value"])
    df["date"] = pd.to_datetime(df["decimal_year"], format="%Y")
    df["station"] = station  # for hover
    return df


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
