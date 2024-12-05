from bokeh.layouts import column, row

# from bokeh.models import CheckboxGroup
from bokeh.models import ColumnDataSource, Button, CustomJS
from bokeh.plotting import figure, curdoc
from bokeh.palettes import Category10

# from bokeh.embed import server_document
from get_solar_data import *

# from callbacks import update_plots, update_error_bars
# from functools import partial
from pathlib import Path


def errorbar(
    fig,
    x,
    y,
    yerr=None,
    color="red",
    point_kwargs={},
    error_kwargs={},
    legend_label=None,
):

    points = fig.line(
        x, y, color=color, legend_label=legend_label, line_width=2, **point_kwargs
    )

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

colors = Category10[10]  # `Category10` can hold up to 10 different colors
series_names = list(data.keys())

# Create a ColumnDataSource for each data series
sources = {name: ColumnDataSource(data=series) for name, series in data.items()}

# Create a figure
plot = figure(
    title="Sunspot Number",
    x_axis_label="Time (years)",
    y_axis_label="Sunspot Number",
    width=1000,
    height=700,
    sizing_mode="scale_both",
)
plot.y_range.start = 0
plot.xaxis.minor_tick_line_color = "black"
plot.xaxis.minor_tick_line_color = "black"
plot.xgrid.grid_line_dash = "dashed"
plot.ygrid.grid_line_dash = "dashed"

# Create plots and error bars for each series and make them initially invisible
plots = {}
for i, (name, source) in enumerate(sources.items()):
    scatter, errors = errorbar(
        plot,
        x=source.data["decimal year"]
        if "decimal year" in source.data
        else source.data["mid year"],
        y=source.data["SNvalue"],
        yerr=None,  # source.data["SNerror"]
        color=colors[i],
        point_kwargs={"alpha": 0.5, "visible": False},
        # error_kwargs={"alpha": 0.5, "line_width": 2, "visible": False},
        legend_label=name,
    )

    plots[name] = {"scatter": scatter}  # , "error_bars": errors

plot.legend.click_policy = "hide"
# Create CheckboxGroup with options
# plot_checkbox_group = CheckboxGroup(labels=series_names, active=[])
# error_checkbox_group = CheckboxGroup(
#     labels=[f"{name} (error bars)" for name in series_names], active=[]
# )

# Attach the callback to checkbox group
# plot_checkbox_group.on_change(
#     "active",
#     partial(
#         update_plots, checkbox=plot_checkbox_group, series=series_names, plots=plots
#     ),
# )
# error_checkbox_group.on_change(
#     "active",
#     partial(
#         update_error_bars,
#         checkbox=error_checkbox_group,
#         series=series_names,
#         plots=plots,
#     ),
# )

# Create a button for downloading visible data
download_csv_button = Button(label="Download CSV Data", button_type="success")
download_txt_button = Button(label="Download TXT Data", button_type="success")

# JavaScript code for downloading data
js_code = (Path(__file__).parent / "callbacks.js").read_text("utf8")

# Attach the CustomJS callback
download_csv_button.js_on_click(
    CustomJS(
        args=dict(
            source=sources,
            plots=plots,
            x_range=plot.x_range,
            y_range=plot.y_range,
            filename="visible_data",
        ),
        code=js_code
        + """
        const x_start = x_range.start;
        const x_end = x_range.end;
        const y_start = y_range.start;
        const y_end = y_range.end;
        downloadAxes(source, filename, x_start, x_end, y_start, y_end, plots, "csv");
        """,
    )
)
download_txt_button.js_on_click(
    CustomJS(
        args=dict(
            source=sources,
            plots=plots,
            x_range=plot.x_range,
            y_range=plot.y_range,
            filename="visible_data",
        ),
        code=js_code
        + """
        const x_start = x_range.start;
        const x_end = x_range.end;
        const y_start = y_range.start;
        const y_end = y_range.end;
        downloadAxes(source, filename, x_start, x_end, y_start, y_end, plots, "txt");
        """,
    )
)

# Layout the components
layout = column(
    # row(plot_checkbox_group, error_checkbox_group),
    plot,
    row(download_csv_button, download_txt_button),
    sizing_mode="stretch_both",
)

# Add the layout to the current document (this makes it live)
curdoc().add_root(layout)

# script = server_document()
# print(script)
