#!/bin/bash

x=`ping -c1 192.168.10.13 2>&1 | grep unreachable`
if [ ! "$x" = "" ]; then
        logger "Serwer monit02 jest down! Probuje obudzic."
        echo  "Serwer monit02 jest down! Probuje obudzic."
        /usr/bin/wakeonlan 00:1e:37:8e:39:c6
        /dane/slack_webhook.sh
fi
