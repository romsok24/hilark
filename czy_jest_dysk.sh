#!/bin/bash

if [[ $(lsblk | grep part | grep T | wc -l) -eq 0 ]]; then  
   echo "Wykryto brak dysku 2T przy Dellu. WYsylam maila" 
   mail -s "Wykryto brak dysku 2T przy kompie do monitorowania" o2o2@gazeta.pl -a 'From: Magazyn MASL'
fi
