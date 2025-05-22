import numpy as np

from bokeh.plotting import figure
from bokeh.models import HoverTool, LinearAxis, Range1d
from PIL import ImageColor, Image, ImageDraw


class HVOPlot:
    def __init__(
        self,
        title: str,
        x_label: str,
        y_label: str,
        y_start_zero: bool = False,
        y_label_color: str = "black",
    ):
        """
        Initialize the HVOPlot class
        Inputs:
            title, title of plot
            x_label, x-axis label
            y_label, y-axis label
            y_start_zero, configure graph to plot starting at y = 0
            y_label_color, configure color of y-axis label
        """

        self.plot = figure(
            title=title,
            x_axis_label=x_label,
            y_axis_label=y_label,
            width=1000,
            height=700,
            sizing_mode="scale_both",
        )

        self.x_label = x_label
        self._configure_axes(y_start_zero, y_label_color)

    def add_y_axis(
        self,
        source,
        legend_label: str,
        y_label: str,
        x_key: str,
        y_key: str,
        color="navy",
        point_kwargs={},
    ):
        """
        Add secondary y-axis
        Inputs:
          source, bokeh ColumnDataSource
          legend_label, name of legend
          y_label, second y-axis label
          x_key, name of x key in source to plot
          y_key, name of y key in source to plot
          color, color of plot
          point_kwargs, optional argument(s) for bokeh line plot
        """

        self.plot.extra_y_ranges["foo"] = Range1d(
            min(source.data[y_key]), max(source.data[y_key])
        )
        ax2 = LinearAxis(y_range_name="foo", axis_label=y_label)
        ax2.axis_label_text_color = color
        self.plot.add_layout(ax2, "right")

        return self.plot.line(
            x_key,
            y_key,
            source=source,
            color=color,
            alpha=0.5,
            line_width=2,
            legend_label=legend_label,
            y_range_name="foo",
            **point_kwargs,
        )

    def _configure_axes(self, y_start_zero: bool, y_lab_color: str):
        """
        Configure the axes
        Input:
          y_start_zero, configure graph to plot starting at y = 0
          y_lab_color, configure color of y-axis label
        """

        if y_start_zero:
            self.plot.y_range.start = 0

        self.plot.xaxis.minor_tick_line_color = "black"
        self.plot.yaxis.minor_tick_line_color = "black"

        self.plot.xgrid.grid_line_dash = "dashed"
        self.plot.ygrid.grid_line_dash = "dashed"

        self.plot.xaxis.axis_label_text_color = "black"
        self.plot.yaxis.axis_label_text_color = y_lab_color

    def add_hover_tool(
        self,
        source,
        x_key: str,
        y_key: str,
        x_label: str,
        y_label: str,
        hover_color: str = "#000080",
    ):
        """
        Add a hover tool to the plot
        Inputs:
            source, bokeh ColumnDataSource containing relevant data
            x_key, name of x key in source to plot
            y_key, name of y key in source to plot
            x_label, label of x-coordinate in HoverTool
            y_label, label of y-coordinate in HoverTool
            hover_color, color of HoverTool. Default color navy. Accepts hex format (#RRGGBB)
        Output,
          hover, bokeh HoverTool object
        """

        renderer = self.plot.circle(
            x_key, y_key, source=source, size=8, color="navy", alpha=0.0
        )
        hover_html = f"""
        <div style="background-color:#f0f8ff; color:{hover_color}; padding:5px; border:1px solid #aaa;">
          <span style="font-size: 14px;"><b>{x_label}:</b> @{x_key}{{0.00}}</span><br>
          <span style="font-size: 14px;"><b>{y_label}:</b> @{y_key}</span>
        </div>
        """
        alpha = 128
        img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        rgba = ImageColor.getcolor(hover_color, "RGB") + (alpha,)
        # vertical bar
        draw.rectangle([13, 0, 19, 32], fill=rgba)
        # horizontal bar
        draw.rectangle([0, 13, 32, 19], fill=rgba)
        hover = HoverTool(tooltips=hover_html, renderers=[renderer], icon=img)

        self.plot.add_tools(hover)

        return hover

    def line_plot(
        self, source, legend_label: str, x: str, y: str, color="navy", point_kwargs={}
    ):
        """
        Add line plot
        Inputs:
            source, bokeh ColumnDataSource containing relevant data
            legend_label, name of legend
            x, key name of x-axis data
            y, key name of y-axis data
            color, color of plot
            point_kwargs, optional argument(s) for bokeh line plot
        """

        return self.plot.line(
            x,
            y,
            source=source,
            color=color,
            alpha=0.5,
            line_width=2,
            legend_label=legend_label,
            **point_kwargs,
        )

    def set_click_policy(self):
        """
        Set click policy for bokeh legend labels
        """

        self.plot.legend.click_policy = "hide"

    def get_plot(self):
        """
        Return HVOPlot class as bokeh plot object (glyph)
        """

        return self.plot
