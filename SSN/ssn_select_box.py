import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Button, CustomJS
from bokeh.plotting import curdoc
from bokeh.palettes import Category10
from pathlib import Path
from plots.hvo_plots import *


# Get data
daily_data = pd.read_pickle("test/SN_d_tot_V2.0.pkl")
monthly_smoothed_data = pd.read_pickle("test/SN_ms_tot_V2.0.pkl")
monthly_data = pd.read_pickle("test/SN_m_tot_V2.0.pkl")
yearly_data = pd.read_pickle("test/SN_y_tot_V2.0.pkl")
data = {
    "Yearly SSN": yearly_data,
    "Monthly SSN": monthly_data,
    "Smoothed SSN": monthly_smoothed_data,
    "Daily SSN": daily_data,
}

colors = Category10[10]  # `Category10` can hold up to 10 different colors
series_names = list(data.keys())

# Create a ColumnDataSource for each data series
sources = {name: ColumnDataSource(data=series) for name, series in data.items()}

# Create a figure
plot = HVOPlot("Sunspot Number", "Time (years)", "Sunspot Number")

# Create plots and error bars for each series and make them initially invisible
plots = {}
for i, (name, source) in enumerate(sources.items()):
    scatter = plot.line_plot(
        source,
        legend_label=name,
        x="decimal year" if "decimal year" in source.data else "mid year",
        y="SNvalue",
        color=colors[i],
        point_kwargs={"visible": False},
    )

    plots[name] = {"scatter": scatter}

plot.set_click_policy()

# Create a button for downloading visible data
download_csv_button = Button(label="Download CSV Data", button_type="success")
download_txt_button = Button(label="Download TXT Data", button_type="success")

# JavaScript code for downloading data
js_callbacks = (
    Path(__file__).parent.parent / "plots" / "callbacks" / "callbacks.js"
).read_text("utf8")

# Attach the CustomJS callback
download_csv_button.js_on_click(
    CustomJS(
        args=dict(
            source=sources,
            plots=plots,
            x_range=plot.get_plot().x_range,
            y_range=plot.get_plot().y_range,
        ),
        code=js_callbacks
        + """
        const x_start = x_range.start;
        const x_end = x_range.end;
        const y_start = y_range.start;
        const y_end = y_range.end;

        // Download data with the visible plot names included
        downloadAxes(
            source,
            x_start,
            x_end,
            y_start,
            y_end,
            plots,
            "csv"
        );
        """,
    )
)

download_txt_button.js_on_click(
    CustomJS(
        args=dict(
            source=sources,
            plots=plots,
            x_range=plot.get_plot().x_range,
            y_range=plot.get_plot().y_range,
        ),
        code=js_callbacks
        + """
        const x_start = x_range.start;
        const x_end = x_range.end;
        const y_start = y_range.start;
        const y_end = y_range.end;

        // Download data with the visible plot names included
        downloadAxes(
            source,
            x_start,
            x_end,
            y_start,
            y_end,
            plots,
            "txt"
        );
        """,
    )
)

# Layout the components
layout = column(
    # row(plot_checkbox_group, error_checkbox_group),
    plot.get_plot(),
    row(download_csv_button, download_txt_button),
    sizing_mode="stretch_both",
)

# Add the layout to the current document (this makes it live)
curdoc().add_root(layout)
