cd /var/www/html/Forecast
source /var/www/html/root/root/bin/thisroot.sh
./PhiJ
python3 Range.py
python3 Format.py
./FF
python3 download.py
cd /var/www/html/Forecast/DTXT
python3 T2.py
python3 comma_APTY.py
python3 comma_HRMR.py
python3 comma_JUNG.py
python3 comma_MOSC.py
python3 comma_MXCO.py
python3 comma_OULU.py
python3 comma_NEWK.py
python3 T2CSV.py
echo "completed"
