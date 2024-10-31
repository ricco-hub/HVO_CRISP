cd /var/www/html/Wilcox_TILT
python3 Range.py
python3 Format.py
source /var/www/html/root/root/bin/thisroot.sh
./TILT
python3 download.py
cd /var/www/html/Wilcox_TILT/DTXT
python3 comma.py
python3 T2.py
python3 T2CSV.py
echo "completed"
