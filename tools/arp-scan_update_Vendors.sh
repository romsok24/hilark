#!/bin/bash

# ########################## Update the list of vebdors
cd /usr/share/arp-scan
sudo get-iab -v -u http://standards.ieee.org/develop/regauth/iab/iab.txt
sudo get-oui -v -u http://standards.ieee.org/develop/regauth/oui/oui.txt

# ######################### If the above will not work- use second method:
# cd /usr/share/arp-scan
# sudo wget http://standards.ieee.org/develop/regauth/oui/oui.txt
# sudo wget http://standards.ieee.org/develop/regauth/iab/iab.txt

# ######################### Examlpe usage
# arp-scan -l --interface enxb827eb2ed20b --timeout 5
