import datetime
from pathlib import Path
from functools import partial

import pandas as pd
from bs4 import BeautifulSoup

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import (
    MultiSelect,
    Select,
    Button,
    PreText,
    ColumnDataSource,
    DateRangePicker,
    CustomJS,
    Legend,
    LegendItem,
    HoverTool,
)
from bokeh.plotting import figure
from bokeh.palettes import Category10

from DECIMAL import decimal_year
from import2 import simple_get  # Custom, retain if needed


# --- Load station metadata ---
base_path = Path("/var/www/ricco_website/HVO_CRISP/NeutronMonitor_Rate")
stations = base_path.joinpath("NMStations.txt").read_text().split()
resolutions = base_path.joinpath("Resolution.txt").read_text().split()
titles = base_path.joinpath("ResT.txt").read_text().split()

# --- UI widgets ---
station_multi_select = MultiSelect(
    title="Stations", value=[stations[0]], options=stations
)
resolution_select = Select(
    title="Resolution", value=resolutions[0], options=resolutions
)
status = PreText(text="Ready")
fetch_button = Button(label="Fetch Data", button_type="primary")
download_csv_button = Button(label="Download CSV", button_type="success")

date_picker = DateRangePicker(
    title="Date Range",
    value=(datetime.date(1960, 1, 1), datetime.date.today()),
    min_date=datetime.date(1960, 1, 1),
    max_date=datetime.date.today(),
)

# --- Plot setup ---
plot = figure(
    title="Neutron Monitor Count Rates",
    x_axis_label="Decimal Year",
    y_axis_label="Count Rate",
    sizing_mode="stretch_both",
    height=400,
    tools="pan,wheel_zoom,box_zoom,reset,save",
)
plot.legend.click_policy = "hide"

sources = {}
colors = Category10[10]
legend_items = []

hover_tool = HoverTool(
    tooltips=[
        ("Station", "@station"),
        ("Decimal Year", "@decimal_year{0.000}"),
        ("Value", "@value{0.00}"),
    ],
    mode="vline",
)
plot.add_tools(hover_tool)

# --- Data Fetching ---


# --- Update Plot ---
def update():
    plot.renderers.clear()
    sources.clear()

    selected_stations = station_multi_select.value
    resolution = resolution_select.value
    color_cycle = iter(colors)

    all_dates = []

    for station in selected_stations:
        df = fetch_data(station, resolution)
        if df.empty:
            continue

        source = ColumnDataSource(df)
        sources[station] = source
        color = next(color_cycle)

        plot.line(
            "decimal_year",
            "value",
            source=source,
            line_width=2,
            color=color,
            legend_label=station,
        )

        all_dates.append(df["date"])

    if all_dates:
        combined = pd.concat(all_dates)
        min_d, max_d = combined.min().date(), combined.max().date()
        date_picker.min_date = min_d
        date_picker.max_date = max_d
        date_picker.value = (min_d, max_d)

    # Move this here AFTER glyphs are added
    plot.legend.click_policy = "hide"

    status.text = f"Loaded {len(selected_stations)} station(s)"


# --- Date Filter ---
def filter_by_date(attr, old, new):
    start, end = (
        pd.to_datetime(date_picker.value[0]),
        pd.to_datetime(date_picker.value[1]),
    )
    for station, src in sources.items():
        df = src.to_df()
        mask = (df["date"] >= start) & (df["date"] <= end)
        src.data = df.loc[mask].to_dict("list")
    status.text = f"Filtered: {start.date()} → {end.date()}"


date_picker.on_change("value", filter_by_date)

# --- CSV Download ---
download_csv_button.js_on_click(
    CustomJS(
        args=dict(sources=sources),
        code="""
        let rows = ["station,decimal_year,value"];
        for (const [station, src] of Object.entries(sources)) {
            const data = src.data;
            for (let i = 0; i < data.decimal_year.length; i++) {
                rows.push(`${station},${data.decimal_year[i]},${data.value[i]}`);
            }
        }
        const blob = new Blob([rows.join("\\n")], { type: "text/csv;charset=utf-8;" });
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "neutron_monitor_data.csv";
        a.click();
        """,
    )
)

# --- Callbacks ---
fetch_button.on_click(update)

# --- Layout ---
layout = column(
    row(station_multi_select, resolution_select),
    row(date_picker, fetch_button, download_csv_button),
    status,
    plot,
    sizing_mode="stretch_both",
)

curdoc().add_root(layout)
update()
curdoc().title = "Neutron Monitor Viewer"


"""
import pandas as pd
import sys
import os

from datetime import datetime
from pathlib import Path
from functools import partial
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, DateRangePicker, Button, CustomJS
from bokeh.plotting import curdoc
from bokeh.palettes import Category10

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from plots.hvo_plots import HVOPlot
from plots.callbacks.callbacks import (
    update_hover_data,
    reset_data_combined,
    sync_hover_tool_icon,
)
from utils.utils import decimal_year_to_YYYYMMDD


# --- Load data ---
density = pd.read_pickle("data/ProtonDensity.pkl")
wind = pd.read_pickle("data/WindSpeed.pkl")

# Create datetime columns
density["date"] = density["decimal_year"].apply(decimal_year_to_YYYYMMDD)
wind["date"] = wind["decimal_year"].apply(decimal_year_to_YYYYMMDD)

# Bundle all data
data_dict = {
    "Proton Density": density,
    "Wind Speed": wind,
}
y_keys = ["ProtonDensity", "WindSpeed"]

# --- Plot setup ---
sources = {}
source_data = {}
plots = {}
colors = Category10[10]
plot = HVOPlot(
    "Solar Wind and Proton Density",
    "Time (years)",
    "Proton Density (N/cm³)",
    y_start_zero=True,
    y_end=15.75,
    y_label_color=colors[0],
)

# Create all line plots
for i, (label, df) in enumerate(data_dict.items()):
    sources[label] = ColumnDataSource(data=df)
    source_data[label] = ColumnDataSource(data=df.drop(columns=["date"]))

    if i == 0:
        scatter = plot.line_plot(
            sources[label],
            legend_label=label,
            x="decimal_year",
            y=y_keys[i],
            color=colors[i],
        )
        hover = plot.add_hover_tool(
            sources[label],
            "decimal_year",
            y_keys[i],
            "Year",
            "Density",
            hover_color=colors[i],
        )
    else:
        scatter = plot.add_y_axis(
            sources[label],
            legend_label=label,
            y_label="Wind Speed (km/s)",
            x_key="decimal_year",
            y_key=y_keys[i],
            color=colors[i],
        )
        hover = plot.add_hover_tool(
            sources[label],
            "decimal_year",
            y_keys[i],
            "Year",
            "Speed",
            hover_color=colors[i],
            renderer=scatter,
        )

    plots[label] = {"scatter": scatter, "hover": hover}

plot.set_click_policy()

# Toggle visibility of HoverTool based on visibility of plots
for label, obj in plots.items():
    obj["scatter"].on_change(
        "visible", partial(sync_hover_tool_icon, plots=plots, plot=plot)
    )

# --- DateRangePicker ---
# Convert to native datetime.date objects
min_date = min(df["date"].min() for df in data_dict.values()).date()
max_date = max(df["date"].max() for df in data_dict.values()).date()

date_range_picker = DateRangePicker(
    title="Select date range manually. Double click to select a date.",
    value=(min_date, max_date),
    min_date=min_date,
    max_date=max_date,
)


# Attach callback to filter all sources
for label, df in data_dict.items():
    date_range_picker.on_change(
        "value",
        partial(
            update_hover_data,
            date_range=date_range_picker,
            data=df,
            source=sources[label],
        ),
    )

# --- Reset button ---
reset_button = Button(label="Reset Plot", button_type="primary")
reset_button.on_click(
    partial(
        reset_data_combined,
        data_dict=data_dict,
        sources=sources,
        date_picker=date_range_picker,
    )
)


# --- Download buttons ---
download_csv_button = Button(label="Download CSV Data", button_type="success")
download_txt_button = Button(label="Download TXT Data", button_type="success")

js_callbacks = (
    Path(__file__).parent.parent / "plots" / "callbacks" / "callbacks.js"
).read_text("utf8")

download_csv_button.js_on_click(
    CustomJS(
        args=dict(
            source=sources,
            plots=plots,
            x_range=plot.get_plot().x_range,
            y_range=plot.get_plot().y_range,
        ),
        code=js_callbacks
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
    )
)

# --- Layout ---
layout = column(
    row(date_range_picker, reset_button),
    plot.get_plot(),
    row(download_csv_button, download_txt_button),
    sizing_mode="stretch_both",
)

curdoc().add_root(layout)
"""

"""
import datetime
from functools import partial

import pandas as pd
import requests
from bs4 import BeautifulSoup

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import Select, Button, PreText, ColumnDataSource
from bokeh.plotting import figure

from DECIMAL import decimal_year
from import2 import simple_get  # Custom, keep if needed

# --- Read Station Metadata ---
with open("/var/www/html/NeutronMonitor_Rate/NMStations.txt") as f:
    stations = f.readline().split()
with open("/var/www/html/NeutronMonitor_Rate/Resolution.txt") as f:
    resolutions = f.readline().split()
with open("/var/www/html/NeutronMonitor_Rate/ResT.txt") as f:
    titles = f.readline().split()

# --- UI Widgets ---
station_select = Select(title="Station", value=stations[0], options=stations)
resolution_select = Select(title="Resolution", value=resolutions[0], options=resolutions)
status = PreText(text="Ready")
fetch_button = Button(label="Fetch Data", button_type="primary")

source = ColumnDataSource(data=dict(decimal_year=[], value=[]))
plot = figure(title="Neutron Monitor Data", x_axis_label="Decimal Year", y_axis_label="Value")
plot.line("decimal_year", "value", source=source)

# --- Data Fetching Function ---
def fetch_data(station, resolution, title):
    now = datetime.datetime.now()
    url = (
        f"http://www.nmdb.eu/nest/draw_graph.php?formchk=1&stations[]={station}"
        f"&tabchoice=1h&dtype=corr_for_efficiency&tresolution={resolution}"
        f"&yunits=0&date_choice=bydate&start_day=1&start_month=1&start_year=1960"
        f"&start_hour=0&start_min=0&end_day={now.day}&end_month={now.month}&end_year={now.year}"
        f"&end_hour=23&end_min=59&output=ascii"
    )
    response = simple_get(url)
    html = BeautifulSoup(response, "html.parser")
    pre_data = html.select("pre")[0].text.splitlines()

    # Skip header lines
    data = []
    for line in pre_data[25:]:
        tokens = line.split()
        try:
            year = int(line[0:4])
            month = int(line[5:7])
            day = int(line[8:10])
            date_decimal = decimal_year(year, month, day)
            value = float(tokens[2] if len(tokens) > 2 else tokens[1][9:])
            data.append((date_decimal, value))
        except Exception as e:
            print("Parsing error:", e, line)

    return pd.DataFrame(data, columns=["decimal_year", "value"])

# --- Callback ---
def update():
    station = station_select.value
    resolution = resolution_select.value
    title = titles[resolutions.index(resolution)]
    status.text = f"Fetching data for {station} ({resolution})..."
    df = fetch_data(station, resolution, title)
    source.data = df.to_dict(orient="list")
    status.text = f"Data updated: {len(df)} points"

fetch_button.on_click(update)

# --- Layout ---
layout = column(
    row(station_select, resolution_select, fetch_button),
    status,
    plot,
)

curdoc().add_root(layout)
curdoc().title = "Neutron Monitor Viewer"

"""

"""
import asyncio
import aiohttp
import datetime
import os
import logging
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from contextlib import asynccontextmanager
from bs4 import BeautifulSoup
import pandas as pd
from DECIMAL import decimal_year

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class StationConfig:
    stations: List[str]
    resolutions: List[str]
    titles: List[str]
    base_path: Path

class NeutronMonitorDataFetcher:

    def __init__(self, config_dir: str = "/var/www/html/NeutronMonitor_Rate"):
        self.config_dir = Path(config_dir)
        self.base_url = "http://www.nmdb.eu/nest/draw_graph.php"
        self.session = None
        self._config = None

    @asynccontextmanager
    async def get_session(self):
        if self.session is None:
            timeout = aiohttp.ClientTimeout(total=30)
            self.session = aiohttp.ClientSession(timeout=timeout)
        try:
            yield self.session
        finally:
            pass  # Keep session alive for reuse

    async def close_session(self):
        if self.session:
            await self.session.close()
            self.session = None

    def load_config(self) -> StationConfig:
        if self._config is not None:
            return self._config

        try:
            stations = self._read_config_file("NMStations.txt")
            resolutions = self._read_config_file("Resolution.txt")
            titles = self._read_config_file("ResT.txt")

            self._config = StationConfig(
                stations=stations,
                resolutions=resolutions,
                titles=titles,
                base_path=self.config_dir
            )
            return self._config

        except FileNotFoundError as e:
            logger.error(f"Configuration file not found: {e}")
            raise
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            raise

    def _read_config_file(self, filename: str) -> List[str]:
        file_path = self.config_dir / filename
        with open(file_path, 'r') as f:
            return f.readline().split()

    def build_url(self, station: str, resolution: str,
                  end_date: Optional[datetime.datetime] = None) -> str:
        if end_date is None:
            end_date = datetime.datetime.now()

        params = {
            'formchk': '1',
            'stations[]': station,
            'tabchoice': '1h',
            'dtype': 'corr_for_efficiency',
            'tresolution': resolution,
            'yunits': '0',
            'date_choice': 'bydate',
            'start_day': '1',
            'start_month': '1',
            'start_year': '1960',
            'start_hour': '0',
            'start_min': '0',
            'end_day': str(end_date.day),
            'end_month': str(end_date.month),
            'end_year': str(end_date.year),
            'end_hour': '23',
            'end_min': '59',
            'output': 'ascii'
        }

        url_params = '&'.join(f"{k}={v}" for k, v in params.items())
        return f"{self.base_url}?{url_params}"

    async def fetch_data(self, url: str) -> Optional[str]:
        try:
            async with self.get_session() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.text()
                    else:
                        logger.warning(f"HTTP {response.status} for URL: {url}")
                        return None
        except asyncio.TimeoutError:
            logger.error(f"Timeout fetching data from: {url}")
            return None
        except Exception as e:
            logger.error(f"Error fetching data: {e}")
            return None

    def parse_html_data(self, html_content: str) -> Optional[str]:
        try:
            soup = BeautifulSoup(html_content, "html.parser")
            pre_tags = soup.select("pre")
            if pre_tags:
                return pre_tags[0].text
            return None
        except Exception as e:
            logger.error(f"Error parsing HTML: {e}")
            return None

    def process_raw_data(self, raw_data: str) -> List[Tuple[float, float]]:
        lines = raw_data.strip().split('\n')
        processed_data = []

        # Skip header lines (first 25 lines)
        data_lines = lines[25:] if len(lines) > 25 else lines

        for line in data_lines:
            try:
                parts = line.split()
                if len(parts) >= 2:
                    # Parse date from first part (format: YYYY-MM-DD)
                    date_str = parts[0]
                    if len(date_str) >= 10:
                        year = int(date_str[:4])
                        month = int(date_str[5:7])
                        day = int(date_str[8:10])

                        # Get value (handle different formats)
                        if len(parts) == 2:
                            value_str = parts[1]
                            if len(value_str) > 9:
                                value = float(value_str[9:])
                            else:
                                value = float(value_str)
                        else:
                            value = float(parts[2])

                        decimal_year_val = decimal_year(year, month, day)
                        processed_data.append((decimal_year_val, value))

            except (ValueError, IndexError) as e:
                logger.debug(f"Skipping malformed line: {line} - {e}")
                continue

        return processed_data

    def save_processed_data(self, data: List[Tuple[float, float]],
                          filepath: Path) -> None:
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w') as f:
                for decimal_year_val, value in data:
                    f.write(f"{decimal_year_val}  {value}\n")
        except Exception as e:
            logger.error(f"Error saving data to {filepath}: {e}")
            raise

    def get_data_as_dataframe(self, data: List[Tuple[float, float]]) -> pd.DataFrame:
        df = pd.DataFrame(data, columns=['decimal_year', 'value'])
        return df.sort_values('decimal_year').reset_index(drop=True)

    async def fetch_station_data(self, station: str, resolution: str,
                               title: str) -> Optional[pd.DataFrame]:
        logger.info(f"Fetching data for station: {station}, resolution: {resolution}")

        try:
            # Build URL and fetch data
            url = self.build_url(station, resolution)
            html_content = await self.fetch_data(url)

            if html_content is None:
                return None

            # Parse and process data
            raw_data = self.parse_html_data(html_content)
            if raw_data is None:
                return None

            processed_data = self.process_raw_data(raw_data)
            if not processed_data:
                logger.warning(f"No valid data found for {station}")
                return None

            # Save to file (optional, for backup)
            filepath = self.config_dir / f"{station}{title}.txt"
            self.save_processed_data(processed_data, filepath)

            # Return as DataFrame for Bokeh use
            return self.get_data_as_dataframe(processed_data)

        except Exception as e:
            logger.error(f"Error processing station {station}: {e}")
            return None

    async def fetch_all_data(self) -> Dict[str, pd.DataFrame]:
        config = self.load_config()
        results = {}

        tasks = []
        for w, (resolution, title) in enumerate(zip(config.resolutions, config.titles)):
            for station in config.stations:
                task_name = f"{station}_{title}"
                task = self.fetch_station_data(station, resolution, title)
                tasks.append((task_name, task))

        # Execute all tasks concurrently
        for task_name, task in tasks:
            try:
                result = await task
                if result is not None:
                    results[task_name] = result
            except Exception as e:
                logger.error(f"Task {task_name} failed: {e}")

        await self.close_session()
        return results

# Usage example for Bokeh server
class NeutronMonitorBokehApp:

    def __init__(self, config_dir: str = "/var/www/html/NeutronMonitor_Rate"):
        self.fetcher = NeutronMonitorDataFetcher(config_dir)
        self.data_cache = {}
        self.last_update = None

    async def update_data(self, force_refresh: bool = False) -> Dict[str, pd.DataFrame]:
        now = datetime.datetime.now()

        # Update if forced or if it's been more than 1 hour
        if (force_refresh or
            self.last_update is None or
            (now - self.last_update).total_seconds() > 3600):

            logger.info("Updating neutron monitor data...")
            self.data_cache = await self.fetcher.fetch_all_data()
            self.last_update = now
            logger.info(f"Updated data for {len(self.data_cache)} datasets")

        return self.data_cache

    def get_station_data(self, station: str, title: str = "") -> Optional[pd.DataFrame]:
        key = f"{station}_{title}" if title else station
        return self.data_cache.get(key)

    def get_available_stations(self) -> List[str]:
        return [key.split('_')[0] for key in self.data_cache.keys()]

# Example usage in a Bokeh server application:
"""
"""
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.layouts import column

# Initialize the app
nm_app = NeutronMonitorBokehApp()

# Create initial plot
p = figure(title="Neutron Monitor Data", x_axis_label="Decimal Year", y_axis_label="Count Rate")
source = ColumnDataSource(data=dict(x=[], y=[]))
line = p.line('x', 'y', source=source)

async def update_plot():
    data = await nm_app.update_data()
    if data:
        # Example: plot first available dataset
        first_key = list(data.keys())[0]
        df = data[first_key]
        source.data = dict(x=df['decimal_year'], y=df['value'])

# Update every hour
curdoc().add_periodic_callback(lambda: asyncio.create_task(update_plot()), 3600000)
curdoc().add_root(column(p))
"""
