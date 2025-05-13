/**
 * Check if a year is a leap year
 *
 * @param {number} year - integer year
 * @returns {number} - returns 365 or 366
 */
function isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}

/**
 * Convert YYYY.YY format to YYYYMMDD
 *
 * @param {Float64Array} decimalYear - decimal year
 * @returns {string} - string in YYYYMMDD format
 */
function decimalYearToYYYYMMDD(decimalYear) {
        // Extract the integer year
        const year = Math.floor(decimalYear);

        // Calculate the fractional part
        const fraction = decimalYear - year;

        // Determine if it's a leap year
        const daysInYear = isLeapYear(year) ? 366 : 365;

        // Convert the fraction to days
        const days = Math.floor(fraction * daysInYear);

        // Create the date object starting from January 1
        const startOfYear = new Date(Date.UTC(year, 0, 1));

        // Add the days to get the final date
        const finalDate = new Date(startOfYear);
        finalDate.setUTCDate(finalDate.getUTCDate() + days);

        // Format as YYYYMMDD
        const yyyy = finalDate.getUTCFullYear();
        const mm = String(finalDate.getUTCMonth() + 1).padStart(2, '0'); // Months are 0-indexed
        const dd = String(finalDate.getUTCDate()).padStart(2, '0');

        return `${yyyy}${mm}${dd}`;
    }

/**
 * Generate a datafile ready for download. Meant to be used for the plot_ssn script
 *
 * @param {*} source - bokeh ColumnDataSource containing SSN data
 * @param {string} format - defines the type of file to download: "csv" or "txt"
 * @returns {Array} data - array of strings of SSN data
 */
function generateFile(source, format) {
    const columns = Object.keys(source.data);
    const rows = source.get_length();
    const data = [];

    if (format === 'csv') {
        // Add header row for CSV
        data.push(columns.join(','));
    } else if (format === 'txt') {
        // Add header row for TXT
        const header = columns.map(col => col.padEnd(15, ' ')); // Fixed-width headers
        data.push(header.join('\t'));
    }

    // Generate data rows
    for (let i = 0; i < rows; i++) {
        const row = columns.map(column => {
            const value = source.data[column][i];
            return format === 'csv' ? value : String(value).padEnd(15, ' ');
        });

        if (format === 'csv') {
            data.push(row.join(',')); // Comma-separated values for CSV
        } else if (format === 'txt') {
            data.push(row.join('\t')); // Tab-separated values for TXT
        }
    }

    // Join rows with newline
    return data.join('\n');
}

/**
 * Function to download data file from plot_ssn script
 *
 * @param {*} source - bokeh ColumnDataSource containing SSN data
 * @param {string} filename - filename of download, e.g., "ssn_data.csv"
 * @param {string} format - defines the type of file to download: "csv" or "txt"
 */
function downloadFile(source, filename, format) {
    // Generate the content based on the format
    const content = generateFile(source, format);

    // Create a Blob and trigger a download
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);

    // Create a temporary <a> element to trigger the download
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();

    // Clean up the URL object
    URL.revokeObjectURL(url);
    document.body.removeChild(a);
}

/**
 * Grab current data on visible axes. Allows users to download data as CSV or TXT file.
 *
 * @param {*} source - bokeh ColumnDataSource containing SSN data
 * @param {*} x_start - data object representing first visible x data point
 * @param {*} x_end - data object representing last visible x data point
 * @param {*} y_start - data object representing first visible y data point
 * @param {*} y_end - data object representing last visible y data point
 * @param {*} plots - python dictionary containing visible axes
 * @param {string} format - file format to be downloaded. Can choose from "csv" or "txt"
 * @param {string} keys - name of input data to determine key naming scheme. Can choose from "SSN"
 */
function downloadAxes(source, x_start, x_end, y_start, y_end, plots, format, keys) {
    format = format || "csv"; // Default format
    let globalMinX = Infinity;
    let globalMaxX = -Infinity;
    var fileName;

    const activePlots = Object.entries(plots).filter(([name, plot]) => plot.scatter.visible);
    const filteredData = activePlots.map(([name, plot]) => {
        const data = source[name].data;

        let xKey;
        let yKey;
        if (keys === "SSN") {
          xKey = 'decimal year' in data ? 'decimal year' : 'mid year';
          yKey = 'SNvalue';
        } else {
          xKey = 'decimal_year';
          yKey = Object.keys(data)[2];
        }

        const filteredIndices = data[xKey].map((x, i) =>
            (x >= x_start && x <= x_end && data[yKey][i] >= y_start && data[yKey][i] <= y_end) ? i : -1
        ).filter(i => i !== -1);

        // Find min and max values for naming file in the format minDate_maxDate.fileType
        // need to find global minima and maxima for multiple datasets (plots)
        const filteredXValues = filteredIndices.map(i => data[xKey][i]);
        if (filteredXValues.length > 0) {
          const localMin = Math.min(...filteredXValues);
          const localMax = Math.max(...filteredXValues);
          if (localMin < globalMinX) globalMinX = localMin;
          if (localMax > globalMaxX) globalMaxX = localMax;
        }

        const filtered = {};
        Object.keys(data).forEach((key) => {
            filtered[key] = filteredIndices.map((i) => data[key][i]);
        });

        return { name, data: filtered };
    });

    const rows = [];
    filteredData.forEach(({ name, data }) => {
        const keys = Object.keys(data);
        rows.push(`Data Series: ${name}`);
        rows.push(keys.join(format === "csv" ? "," : "\t"));

        const numRows = data[keys[0]].length;
        for (let i = 0; i < numRows; i++) {
            const row = keys.map((key) => {
                let value = data[key][i];
                if (key === 'decimal year' || key === 'mid year' || key === 'decimal_year' && format === "txt") {
                    value = value.toFixed(3);
                }
                return value ?? "";
            });
            rows.push(row.join(format === "csv" ? "," : "\t"));
        }
        rows.push('');
    });

    // Make file name
    if (isFinite(globalMinX) && isFinite(globalMaxX)) {
      const formatMin = decimalYearToYYYYMMDD(globalMinX);
      const formatMax = decimalYearToYYYYMMDD(globalMaxX);

      // Get names of visible plots
      const visiblePlotNames = Object.keys(plots).filter(name => {
        return plots[name].scatter.visible;
      });

      if (visiblePlotNames.length === 0) {
        alert("No visible plots to download.");
        return;
      }

      // Combine visible plot names into a string
      const visibleHeader = "Visible Plots: " + visiblePlotNames.join(", ");

      // Update file name with visible plots
      const plotNames = visiblePlotNames.join("_");
      const startEndFileName = `_${formatMin}_${formatMax}`;

      fileName = plotNames.concat(startEndFileName);
    }

    const content = rows.join('\n');
    const mimeType = format === "csv" ? "text/csv" : "text/plain";
    const fileExtension = format === "csv" ? "csv" : "txt";

    const blob = new Blob([content], { type: `${mimeType};charset=utf-8;` });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `${fileName}.${fileExtension}`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
