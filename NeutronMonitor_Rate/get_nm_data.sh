#!/bin/bash


# Get current time
YEAR=$(date +%Y)
MONTH=$(date +%m)
DAY=$(date +%d)

# Output directory
OUTDIR="/var/www/ricco_website/HVO_CRISP/NeutronMonitor_Rate/data"
mkdir -p "$OUTDIR"

# Define stations and resolutions
stations=("OULU" "NEWK" "APTY" "JUNG" "HRMS" "MOSC" "MXCO")
resolutions=(1440 39276 525969)  # 1 day, 1 Carrington rotation, 1 year
# 1 month not supported

# Base URL
base_url="https://www.nmdb.eu/nest/draw_graph.php"

# Fixed query parameters
#common_params="date_choice=last&last_days=1&last_label=days_label&yunits=0&yscale=0&output=ascii&wget=1"

# Loop over stations and resolutions
for station in "${stations[@]}"; do
  for res in "${resolutions[@]}"; do
    url="${base_url}?stations[]=${station}&tabchoice=revori&dtype=corr_for_efficiency&tresolution=${res}&date_choice=bydate&start_day=3&start_month=6&start_year=1951&start_hour=0&start_min=0&end_day=${DAY}&end_month=${MONTH}&end_year=${YEAR}&end_hour=23&end_min=59&yunits=0&yscale=0&output=ascii&wget=1"
    # doesn't like when I do tresolution=${res}
    #url="${base_url}?${common_params}&stations[]=${station}&tresolution=${res}"
    outfile="${OUTDIR}/${station}_${res}.txt"
    wget -np -q -O "$outfile" "$url"
  done
done
