from bokeh.layouts import column, row
from bokeh.models import CheckboxGroup, ColumnDataSource, Button, CustomJS
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
    scatter, errors = errorbar(
        plot,
        x=source.data["decimal year"]
        if "decimal year" in source.data
        else source.data["mid year"],
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
    labels=[f"{name} (error bars)" for name in series_names], active=[]
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

# Create a button for downloading visible data
download_csv_button = Button(label="Download CSV Data", button_type="success")
download_txt_button = Button(label="Download TXT Data", button_type="success")

# JavaScript code for downloading data
download_csv_code = """
const visiblePlots = [];
for (const [name, plotObj] of Object.entries(plots)) {
    if (plotObj.scatter.visible) {
        const source = sources[name];
        const data = source.data;
        const keys = Object.keys(data);
        const rows = [];

        // Convert data into rows
        for (let i = 0; i < data[keys[0]].length; i++) {
            const row = {};
            keys.forEach(key => row[key] = data[key][i]);
            rows.push(row);
        }

        // Add rows to visiblePlots array
        rows.forEach(row => {
            row['Dataset'] = name; // Add dataset name for context
            visiblePlots.push(row);
        });
    }
}

// Generate CSV if there are visible plots
if (visiblePlots.length > 0) {
    const csv = [
        Object.keys(visiblePlots[0]).join(','),  // Header
        ...visiblePlots.map(row => Object.values(row).join(','))  // Rows
    ].join('\\n');

    // Trigger download
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'visible_data.csv';
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
} else {
    alert("No visible data to download.");
}
"""

download_txt_code = """
const visiblePlots = [];
for (const [name, plotObj] of Object.entries(plots)) {
    if (plotObj.scatter.visible) {
        const source = sources[name];
        const data = source.data;
        const keys = Object.keys(data);
        const rows = [];

        // Convert data into rows
        for (let i = 0; i < data[keys[0]].length; i++) {
            const row = {};
            keys.forEach(key => row[key] = data[key][i]);
            rows.push(row);
        }

        // Add rows to visiblePlots array
        rows.forEach(row => {
            row['Dataset'] = name; // Add dataset name for context
            visiblePlots.push(row);
        });
    }
}

// Generate TXT content if there are visible plots
if (visiblePlots.length > 0) {
    // Generate header
    const keys = Object.keys(visiblePlots[0]);
    let txt = `# Data from visible plots\\n`;
    txt += keys.join('\\t') + '\\n';  // Tab-delimited header

    // Generate rows
    visiblePlots.forEach(row => {
        const values = keys.map(key => row[key]);
        txt += values.join('\\t') + '\\n';  // Tab-delimited rows
    });

    // Trigger download
    const blob = new Blob([txt], { type: 'text/plain;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'visible_data.txt';
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
} else {
    alert("No visible data to download.");
}
"""

# Attach the CustomJS callback
download_csv_button.js_on_click(
    CustomJS(args=dict(sources=sources, plots=plots), code=download_csv_code)
)

download_txt_button.js_on_click(
    CustomJS(args=dict(sources=sources, plots=plots), code=download_txt_code)
)

# Layout the components
layout = column(
    row(plot_checkbox_group, error_checkbox_group),
    plot,
    row(download_csv_button, download_txt_button),
    sizing_mode="stretch_both",
)

# Add the layout to the current document (this makes it live)
curdoc().add_root(layout)

# script = server_document()
# print(script)
