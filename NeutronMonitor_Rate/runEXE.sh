cd /var/www/html/NeutronMonitor_Rate
python3 Range.py
python3 Format.py
source /var/www/html/root/root/bin/thisroot.sh

#!/bin/bash
input="/var/www/html/NeutronMonitor_Rate/Res.txt"
while IFS= read -r line
do
  echo "$line"
  if [ "$line" = "day" ]; then
    ./MONITOR_RANGE_day
  fi
  if [ "$line" = "month" ]; then
    ./MONITOR_RANGE_month
  fi
  if [ "$line" = "year" ]; then
    ./MONITOR_RANGE_year
  fi
  if [ "$line" = "carr" ]; then
    ./MONITOR_RANGE_carr
  fi

done < "$input"

python3 download.py
cd /var/www/html/NeutronMonitor_Rate/DTXT
python3 comma_APTY.py
python3 comma_HRMS.py
python3 comma_JUNG.py
python3 comma_MOSC.py
python3 comma_MXCO.py
python3 comma_NEWK.py
python3 comma_OULU.py
python3 T2.py
python3 T2CSV.py
echo "completed"
