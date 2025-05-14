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
