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
 * Grab current data on visible axes. Currently used in ssn_select_box but might be scaled to other scripts.
 * Allows users to download data as CSV or TXT file.
 *
 * @param {*} source - bokeh ColumnDataSource containing SSN data
 * @param {string} filename - name of downloaded file
 * @param {*} x_start - data object representing first visible x data point
 * @param {*} x_end - data object representing last visible x data point
 * @param {*} y_start - data object representing first visible y data point
 * @param {*} y_end - data object representing last visible y data point
 * @param {*} plots - python dictionary containing visible axes
 * @param {string} format - file format to be downloaded. Can choose from "csv" or "txt"
 */
function downloadAxes(source, filename, x_start, x_end, y_start, y_end, plots, format) {
    format = format || "csv"; // Default format

    const activePlots = Object.entries(plots).filter(([name, plot]) => plot.scatter.visible);
    const filteredData = activePlots.map(([name, plot]) => {
        const data = source[name].data;
        const xKey = 'decimal year' in data ? 'decimal year' : 'mid year';
        const yKey = 'SNvalue';

        const filteredIndices = data[xKey].map((x, i) =>
            (x >= x_start && x <= x_end && data[yKey][i] >= y_start && data[yKey][i] <= y_end) ? i : -1
        ).filter(i => i !== -1);

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
                if (key === 'decimal year' || key === 'mid year' && format === "txt") {
                    value = value.toFixed(3);
                }
                return value ?? "";
            });
            rows.push(row.join(format === "csv" ? "," : "\t"));
        }
        rows.push('');
    });

    const content = rows.join('\n');
    const mimeType = format === "csv" ? "text/csv" : "text/plain";
    const fileExtension = format === "csv" ? "csv" : "txt";

    const blob = new Blob([content], { type: `${mimeType};charset=utf-8;` });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `${filename}.${fileExtension}`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
