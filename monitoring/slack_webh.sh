#!/bin/bash

. $(dirname "$0")/.psikuta

curl -X POST --data-urlencode "payload={\"channel\": \"#kamery-monitoring\", \"username\": \"Magazyn\", \"text\": \"<@imie.nazwisk> Wykryłem ruch w obszarze monitoringu: $1 ( id=$2 )\", \"icon_emoji\": \":flashlight:\"}" $slack_webhook_mag

/etc/motioneye/slack_sendf.sh $1 $2
