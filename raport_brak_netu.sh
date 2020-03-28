#/bin/bash

echo "Ponizej raport wystepowania zanikow dostawy internetu pod adresem Maslomiaca, ul. Modrzewiowa 2a"
cat /var/log/syslog*1 /var/log/syslog |  grep "cannot ping address 8.8.8.8" |  awk '{print "Dnia "$1" "$2", godz "$3}' | awk -F':' '{print $1":"$2}' | sort -k3 -r
zcat /var/log/syslog*gz |  grep "cannot ping address 8.8.8.8" | sort -r | awk '{print "Dnia "$1" "$2", godz "$3}' | awk -F':' '{print $1":"$2}'

echo "Rapot zostal wygenerowany automatycznie."
echo "Prosze na niego nie odpowiadac."
