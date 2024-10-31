cd /var/www/html/SSN
python3 Range.py
python3 Format.py
source /var/www/html/root/root/bin/thisroot.sh
./SunSpot
python3 download.py
cd /var/www/html/SSN/DTXT
python3 T2.py
python3 comma1.py
python3 comma2.py
python3 comma3.py
python3 comma4.py
python3 T2CSV.py
echo "completed"
