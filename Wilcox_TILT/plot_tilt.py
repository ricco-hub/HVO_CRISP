import pandas as pd
import sys
import os
from pathlib import Path
from datetime import datetime

from bokeh.models import ColumnDataSource, DateRangePicker, Button, CustomJS
from bokeh.layouts import column, row
from bokeh.io import curdoc
from bokeh.palettes import Category10
from functools import partial

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plots.hvo_plots import HVOPlot
from utils.utils import decimal_year_to_YYYYMMDD
from plots.callbacks.callbacks import reset_all, update_all_sources

# --- Define file mapping ---
pkl_files = [
    "data/Tilt_L_n.pkl",
    "data/Tilt_R_n.pkl",
    "data/Tilt_L_s.pkl",
    "data/Tilt_R_s.pkl",
    "data/Tilt_L_av.pkl",
    "data/Tilt_R_av.pkl",
]

# --- Load all data ---
data = {}
source_data = {}
plots = {}

colors = Category10[10]

main_plot = HVOPlot(
    "Tilt Angle of Heliospheric Current Sheet", "Time (years)", "Angle (degrees)"
)

for idx, file_path in enumerate(pkl_files):
    label = Path(file_path).stem.replace("Tilt_", "")  # e.g., "L_av"
    y_key = label
    df = pd.read_pickle(file_path)
    df["date"] = df["decimal_year"].apply(decimal_year_to_YYYYMMDD)

    data[label] = df
    source = ColumnDataSource(data={col: df[col] for col in df.columns})
    source_data[label] = source

    color = colors[idx % len(colors)]
    main_plot.line_plot(source, label, "decimal_year", y_key, color=color)
    main_plot.add_hover_tool(source, "decimal_year", y_key, "Year", f"{label} Angle")
    line = main_plot.line_plot(source, label, "decimal_year", y_key, color=color)
    plots[label] = {"source": source, "renderer": line}

# --- Use one dataset (first) for filtering/resetting ---
initial_label = list(data.keys())[0]
initial_df = data[initial_label]

# --- Date range picker ---
min_date = min(initial_df["date"]).date()
max_date = max(initial_df["date"]).date()
date_range_picker = DateRangePicker(
    title="Select date range manually. Double click to select a date.",
    value=(min_date, max_date),
    min_date=min_date,
    max_date=max_date,
)

date_range_picker.on_change(
    "value",
    partial(
        update_all_sources,
        date_range=date_range_picker,
        data_dict=data,
        sources_dict=source_data,
    ),
)

reset_button = Button(label="Reset Plot", button_type="primary")
reset_button.on_click(
    partial(reset_all, min_date, max_date, date_range_picker, data, source_data)
)

# --- Download buttons ---
download_csv_button = Button(label="Download CSV Data", button_type="success")
download_txt_button = Button(label="Download TXT data", button_type="success")

js_callbacks = (
    Path(__file__).parent.parent / "plots" / "callbacks" / "callbacks.js"
).read_text("utf8")

download_csv_button.js_on_click(
    CustomJS(
        args=dict(
            plots=plots,
            x_range=main_plot.get_plot().x_range,
            y_range=main_plot.get_plot().y_range,
        ),
        code=js_callbacks
        + """
        const x_start = x_range.start;
        const x_end = x_range.end;
        const y_start = y_range.start;
        const y_end = y_range.end;

        downloadAxesTilt(plots, x_start, x_end, y_start, y_end, "csv");
       """,
    )
)

download_txt_button.js_on_click(
    CustomJS(
        args=dict(
            plots=plots,
            x_range=main_plot.get_plot().x_range,
            y_range=main_plot.get_plot().y_range,
        ),
        code=js_callbacks
        + """
        const x_start = x_range.start;
        const x_end = x_range.end;
        const y_start = y_range.start;
        const y_end = y_range.end;

        downloadAxesTilt(plots, x_start, x_end, y_start, y_end, "txt");
       """,
    )
)

# --- Final layout ---
layout = column(
    row(date_range_picker, reset_button),
    main_plot.get_plot(),
    row(download_csv_button, download_txt_button),
    sizing_mode="stretch_both",
)

curdoc().add_root(layout)
