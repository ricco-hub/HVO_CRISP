import requests
import pandas as pd

from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool
from io import StringIO

URL = "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt"


# Function to scrape data from a remote txt file
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
        "Status"
    ]

    data = pd.read_csv(
        StringIO(response.text),
        header=None,
        names=column_data,
        sep=r"\s+",
        dtype={"Status": str},
        low_memory=False
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
    sizing_mode='stretch_both',
    width=1000,
    height=700
)
plot.scatter("dec_year", "sn_value", source=source, size=8, color="navy", alpha=0.5) # make dec_year more human readable

# create hover tool
renderer = plot.circle("dec_year", "sn_value", source=source, size=8, color="navy", alpha=0.5) # currently rounding values

hover = HoverTool(tooltips=[
    ("Year", "@dec_year"),
    ("SSN", "@sn_value")
], renderers=[renderer])

plot.add_tools(hover)

# write to HTML file
output_file("/var/www/ricco_website/HVO_CRISP/SSN/bokeh_test_plot.html")

save(plot)
