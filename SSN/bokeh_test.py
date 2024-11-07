import requests
import pandas as pd

from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import layout
from io import StringIO

URL = "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt"


# Function to scrape data from a remote CSV file
def fetch_data():
    response = requests.get(URL)
    response.raise_for_status()  # Raise an error if the request fails

    # Convert the CSV data to a DataFrame
    column_data = [
        "year",
        "month",
        "day",
        "decimal year",
        "SNvalue",
        "SNerror",
        "Nb observations",
        "Status",
    ]

    data = pd.read_csv(
        StringIO(response.text),
        header=None,
        names=column_data,
        sep=r"\s+",
        dtype={"Status": str},
        low_memory=False,
    )
    # Remove asterisks from Status and convert to numeric
    data["Status"] = pd.to_numeric(
        data["Status"].str.replace("*", "1"), errors="coerce"
    )
    data["Status"] = data["Status"].fillna(0)
    data = data[~data["SNvalue"].isin([-1, -1.0])]
    return data


# Fetch the data
data = fetch_data()

# Set up the data source for Bokeh
source = ColumnDataSource(
    data=dict(dec_year=data["decimal year"], sn_value=data["SNvalue"])
)

# Create a scatter plot
plot = figure(
    title="Sunspot Number",
    x_axis_label="Time (decimal year)",
    y_axis_label="Sunspot Number",
    width=1000,
    height=600,
)
plot.scatter("dec_year", "sn_value", source=source, size=8, color="navy", alpha=0.5)

# Organize the layout
layout = layout([plot])

# Add the layout to the current document
curdoc().add_root(layout)
curdoc().title = "Scraped Data Scatter Plot"

print("Bokeh server is running on http://localhost:5006/bokeh_test")
