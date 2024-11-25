import pandas as pd

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, DateRangePicker
from bokeh.layouts import column
from bokeh.io import curdoc
from datetime import datetime
from callbacks import update_hover_data
from functools import partial
from get_solar_data import *

URL = "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt"


df = fetch_data(URL, COL_DATA_DAILY)
# Using pd.to_datetime to create a datetime object
df["date"] = pd.to_datetime(df[["year", "month", "day"]])

source = ColumnDataSource(
    data=dict(
        dec_year=df["decimal year"],
        sn_value=df["SNvalue"],
        date=df["date"],
        year=df["year"],
    )
)

# Create a scatter plot
plot = figure(
    title="Sunspot Number",
    x_axis_label="Time (decimal year)",
    y_axis_label="Sunspot Number",
    width=1000,
    height=700,
    sizing_mode="scale_both",
)
plot.scatter(
    "dec_year", "sn_value", source=source, size=8, color="navy", alpha=0.5
)  # make dec_year more human readable

# create hover tool
renderer = plot.circle(
    "dec_year", "sn_value", source=source, size=8, color="navy", alpha=0.0
)

hover = HoverTool(
    tooltips=[("Year", "@dec_year"), ("SSN", "@sn_value")], renderers=[renderer]
)  # dec_year rounding

plot.add_tools(hover)

# Create DateRangeSlider
min_date = datetime(1818, 1, 1).date()
max_date = max(df["date"]).date()
date_range_picker = DateRangePicker(
    title="Select data range manually. Double click to select a date.",
    value=(min_date, max_date),
    min_date=min_date,
    max_date=max_date,
)

# Attach Callback to the DateRangeSlider
date_range_picker.on_change(
    "value",
    partial(update_hover_data, date_range=date_range_picker, data=df, source=source),
)

layout = column(date_range_picker, plot, sizing_mode="stretch_both")
curdoc().add_root(layout)
