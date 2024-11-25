from bokeh.layouts import column, row
from bokeh.models import CheckboxGroup, ColumnDataSource
from bokeh.plotting import figure, curdoc
from bokeh.palettes import Category10
from bokeh.embed import server_document
from get_solar_data import *
from callbacks import update_plots, update_error_bars
from functools import partial


def errorbar(fig, x, y, yerr=None, color="red", point_kwargs={}, error_kwargs={}):

    points = fig.circle(x, y, color=color, **point_kwargs)

    error_lines = []

    if yerr is not None:
        y_err_x = []
        y_err_y = []
        for px, py, err in zip(x, y, yerr):
            y_err_x.append((px, px))
            y_err_y.append((py - err, py + err))
        errors = fig.multi_line(y_err_x, y_err_y, color=color, **error_kwargs)
        error_lines.append(errors)

    return points, error_lines


# Get data
temp_data = scrape_all_sources(URLS, COLUMNS)
data = update_cols(temp_data)

# Use a color palette. The number of colors should match the number of data series.
colors = Category10[10]  # `Category10` can hold up to 10 different colors
series_names = list(data.keys())

# Ensure the number of colors matches the number of series
if len(colors) < len(series_names):
    raise ValueError("Not enough colors for the number of data series!")

# Create a ColumnDataSource for each data series
sources = {name: ColumnDataSource(data=series) for name, series in data.items()}

# Create a figure
plot = figure(
    title="Sunspot Number",
    x_axis_label="Time (decimal year)",
    y_axis_label="Sunspot Number",
    width=1000,
    height=700,
    sizing_mode="scale_both",
)

# Create plots and error bars for each series and make them initially invisible
plots = {}
for i, (name, source) in enumerate(sources.items()):
    if name == "Yearly SSN":
        scatter, errors = errorbar(
            plot,
            x=source.data["mid year"],
            y=source.data["SNvalue"],
            yerr=source.data["SNerror"],
            color=colors[i],
            point_kwargs={"size": 8, "alpha": 0.5, "visible": False},
            error_kwargs={"line_width": 1, "visible": False},
        )
    else:
        scatter, errors = errorbar(
            plot,
            x=source.data["decimal year"],
            y=source.data["SNvalue"],
            yerr=source.data["SNerror"],
            color=colors[i],
            point_kwargs={"size": 8, "alpha": 0.5, "visible": False},
            error_kwargs={"line_width": 1, "visible": False},
        )

    plots[name] = {"scatter": scatter, "error_bars": errors}

# Create CheckboxGroup with options
plot_checkbox_group = CheckboxGroup(labels=series_names, active=[])
error_checkbox_group = CheckboxGroup(
    labels=[f"{name} (errors)" for name in series_names], active=[]
)

# Attach the callback to checkbox group
plot_checkbox_group.on_change(
    "active",
    partial(
        update_plots, checkbox=plot_checkbox_group, series=series_names, plots=plots
    ),
)
error_checkbox_group.on_change(
    "active",
    partial(
        update_error_bars,
        checkbox=error_checkbox_group,
        series=series_names,
        plots=plots,
    ),
)

# Layout the components
layout = column(
    row(plot_checkbox_group, error_checkbox_group), plot, sizing_mode="stretch_both"
)

# Add the layout to the current document (this makes it live)
curdoc().add_root(layout)

# script = server_document()
# print(script)
