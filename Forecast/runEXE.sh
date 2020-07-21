cd /var/www/html/Forecast
source /var/www/html/root/root/bin/thisroot.sh
./PhiJ
python3 Range.py
python3 Format.py
./FF
python3 download.py
cd /var/www/html/Forecast/DTXT
python3 T2.py
echo "completed"
