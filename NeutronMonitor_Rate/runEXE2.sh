cd /var/www/html/NeutronMonitor_Rate
python3 Range.py
python3 Format.py
source /var/www/html/root/root/bin/thisroot.sh
./MONITOR_RANGE_month
python3 download.py
cd /var/www/html/NeutronMonitor_Rate/DTXT
python3 T2.py
echo "completed"
