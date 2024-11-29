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
 * Generate a datafile ready for download. Meant to be used for the ssn_select_box script
 *
 * @param {*} sources - bokeh ColumnDataSource containing SSN data
 * @param {*} plots - python dictionary of plots
 * @param {string} format - defines the type of file to download: "csv" or "txt"
 * @returns {string} data - SSN data in the form of a string
 */
function downloadData(sources, plots, format) {
    const visiblePlots = [];
    for (const [name, plotObj] of Object.entries(plots)) {
        if (plotObj.scatter.visible) {
            const source = sources[name];
            const data = source.data;
            const rows = [];
            const keys = Object.keys(data);

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

    if (visiblePlots.length > 0) {
        let outputData = "";

        if (format === 'csv') {
            outputData = [
                Object.keys(visiblePlots[0]).join(','),  // Header
                ...visiblePlots.map(row => Object.values(row).join(','))  // Rows
            ].join('\n');
        } else if (format === 'txt') {
            // Generate header
            const keys = Object.keys(visiblePlots[0]);
            let txt = `# Data from visible plots\n`;
            txt += keys.join('\t') + '\n'; // Tab-delimited header

            // Generate rows
            visiblePlots.forEach(row => {
                const values = keys.map(key => row[key]);
                txt += values.join('\t') + '\n'; // Tab-delimted rows
            });

            outputData = txt
        }

        return outputData;
    } else {
        alert("No visible data to download.");
        return null;
    }
}

/**
 * Generic function to download data file from either plot_ssn or ssn_select_box script
 *
 * @param {*} source - bokeh ColumnDataSource containing SSN data
 * @param {string} filename - filename of download, e.g., "ssn_data.csv"
 * @param {string} format - defines the type of file to download: "csv" or "txt"
 * @param {*} plots - python dictionary of plots
 */
function downloadFile(source, filename, format, plots) {
    // Generate the content based on the format
    let content;

    if (plots === null) {
        content = generateFile(source, format);
    } else if (plots !== null) {
        content = downloadData(source, plots, format);
    }

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
 * Reusable function to trigger a download, which is called in python scripts plot_ssn and ssn_select_box
 *
 * @param {*} source - bokeh ColumnDataSource containing SSN data
 * @param {string} filename - filename of download, e.g., "ssn_data.csv"
 * @param {string} format - defines the type of file to download: "csv" or "txt"
 * @param {*} plots - python dictionary of plots
 */
function triggerDownload(source, filename, format, plots) {
    downloadFile(source, filename, format, plots);
}
