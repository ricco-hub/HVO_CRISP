import os
import pickle
import sys
import requests
import pandas as pd

from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.utils import day_year_to_decimal_year


# --- Config ---
base_dir = "/var/www/ricco_website/HVO_CRISP/WIND/data"
os.makedirs(base_dir, exist_ok=True)
data_url = "https://spdf.gsfc.nasa.gov/pub/data/omni/low_res_omni/omni_27_av.dat"
data_path = os.path.join(base_dir, "omni_27_av.dat")

# --- Download data file ---
response = requests.get(data_url)
with open(data_path, "w") as f:
    f.write(response.text)

# --- Read lines ---
with open(data_path, "r") as f:
    lines = f.readlines()

# --- Parse lines ---
wind_speed_data = []
proton_density_data = []

for line in lines:
    try:
        fields = line.strip().split()
        if len(fields) < 55:
            continue  # Skip incomplete lines

        iYear = int(fields[0])
        iDay = int(fields[1])
        WindSpeed = float(fields[24])
        ProtonDensity = float(fields[23])
        fYear = day_year_to_decimal_year(iDay, iYear)

        if 0 < WindSpeed < 9999:
            wind_speed_data.append([fYear, WindSpeed])

        if 0 < ProtonDensity < 999:
            proton_density_data.append([fYear, ProtonDensity])

    except Exception as e:
        print(f"Skipping line due to error: {e}")
        continue

# --- Save results ---
df_speed = pd.DataFrame(wind_speed_data, columns=["decimal_year", "WindSpeed"])
df_proton = pd.DataFrame(proton_density_data, columns=["decimal_year", "ProtonDensity"])

with open(os.path.join(base_dir, "WindSpeed.pkl"), "wb") as f:
    pickle.dump(df_speed, f)

with open(os.path.join(base_dir, "ProtonDensity.pkl"), "wb") as f:
    pickle.dump(df_proton, f)
