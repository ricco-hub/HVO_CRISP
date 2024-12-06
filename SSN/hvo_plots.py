from bokeh.plotting import figure
from bokeh.models import HoverTool


class HVOPlot:
    def __init__(self, title: str, x_label: str, y_label: str):
        """
        Initialize the HVOPlot class
        Inputs:
            title: title of plot
            x_label: x-axis label
            y_label: y-axis label
        """

        self.plot = figure(
            title=title,
            x_axis_label=x_label,
            y_axis_label=y_label,
            width=1000,
            height=700,
            sizing_mode="scale_both",
        )

        self._configure_axes()

    def _configure_axes(self):
        """Configure the axes."""

        self.plot.y_range.start = 0

        self.plot.xaxis.minor_tick_line_color = "black"
        self.plot.yaxis.minor_tick_line_color = "black"

        self.plot.xgrid.grid_line_dash = "dashed"
        self.plot.ygrid.grid_line_dash = "dashed"

    def add_hover_tool(self, source):
        """
        Add a hover tool to the plot.
        Input:
            source: bokeh ColumnDataSource containing relevant data
        """

        renderer = self.plot.circle(
            "dec_year", "sn_value", source=source, size=8, color="navy", alpha=0.0
        )
        hover = HoverTool(
            tooltips=[("Year", "@dec_year{0.00}"), ("SSN", "@sn_value")],
            renderers=[renderer],
        )

        self.plot.add_tools(hover)

    def line_plot(self, x: str, y: str, source):
        """
            Add line plot
            Inputs:
                x: key name of x-axis data
                y: key name of y-axis data
                source: bokeh ColumnDataSource containing relevant data
        """

        self.plot.line(x, y, source=source, color="navy", alpha=0.5, line_width=2)

    def get_plot(self):
        return self.plot
