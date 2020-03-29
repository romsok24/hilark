#!/bin/bash

. $(dirname "$0")/.psikuta

co_wyslac=$(find /kamery2TB/$(date +'%Y-%m-%d')_$1/ -iname "*_$2*" | head -n1)
echo "Znalazlem taki plik: $co_wyslac"
if [[ $co_wyslac != $(cat /etc/motioneye/slack_sendf.lock) ]]; then
  echo "To jest nowe zdarzenie - wysylam zdjecie na Slacka"
  curl -F file=@$co_wyslac -F "initial_comment=Jeden z kilku obrazów z tego wydarzenia wykrycia ruchu poniżej:" -F channels=C010EGWMZGC -H "Authorization: Bearer $slack_token_wysylanie" https://slack.com/api/files.upload
fi
echo $co_wyslac > /etc/motioneye/slack_sendf.lock 
