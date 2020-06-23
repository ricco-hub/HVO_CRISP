cd FFModel
source /var/www/html/root/root/bin/thisroot.sh
./FF
python3 download.py
cd /var/www/html/Neutron
./Neutron
python3 download.py
echo "completed"
