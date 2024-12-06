import pandas as pd
from hvo_plots import *

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, DateRangePicker, Button, CustomJS
from bokeh.layouts import column, row
from bokeh.io import curdoc
from datetime import datetime
from callbacks import update_hover_data, reset_data
from functools import partial
from pathlib import Path


df = pd.read_pickle("test/SN_d_tot_V2.0.pkl")
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
ssn_plot = HVOPlot("Daily Sunspot Number", "Time (years)", "Sunspot Number")
ssn_plot.line_plot("dec_year", "sn_value", source)
ssn_plot.add_hover_tool(source)

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

# Reset button
reset_button = Button(label="Reset Data", button_type="primary")

reset_button.on_click(
    partial(reset_data, original_data=df, date_picker=date_range_picker)
)

# Download button
download_csv_button = Button(label="Download CSV Data", button_type="success")
download_txt_button = Button(label="Download TXT data", button_type="success")


# CustomJS for downloading data
js_callbacks = (Path(__file__).parent / "callbacks.js").read_text("utf8")
js_utils = (Path(__file__).parent / "utils.js").read_text("utf8")

download_csv_button.js_on_click(
    CustomJS(
        args=dict(source=source, format="csv"),
        code=js_callbacks
        + js_utils
        + """
        const data = source.data;
        const dates = data['dec_year'];
        const minValue = dates.reduce((min, current) => Math.min(min, current), Infinity);
        const maxValue = dates.reduce((max, current) => Math.max(max, current), -Infinity);

        const formatMin = decimalYearToYYYYMMDD(minValue);
        const formatMax = decimalYearToYYYYMMDD(maxValue);
        const fileName = `${formatMin}_${formatMax}_daily_ssn_data.csv`;
        downloadFile(source, fileName, format);
        """,
    )
)
download_txt_button.js_on_click(
    CustomJS(
        args=dict(source=source, format="txt"),
        code=js_callbacks
        + js_utils
        + """
        const data = source.data;
        const dates = data['dec_year'];
        const minValue = dates.reduce((min, current) => Math.min(min, current), Infinity);
        const maxValue = dates.reduce((max, current) => Math.max(max, current), -Infinity);

        const formatMin = decimalYearToYYYYMMDD(minValue);
        const formatMax = decimalYearToYYYYMMDD(maxValue);
        const fileName = `${formatMin}_${formatMax}_daily_ssn_data.txt`;
        downloadFile(source, fileName, format);
        """,
    )
)

layout = column(
    row(date_range_picker, reset_button),
    ssn_plot.get_plot(),
    row(download_csv_button, download_txt_button),
    sizing_mode="stretch_both",
)
curdoc().add_root(layout)
