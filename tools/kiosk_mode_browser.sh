#!/bin/sh

# /etc/xdg/lxsession/LXDE-pi/autostart

xset -dpms # disable DPMS (Energy Star) features.
xset s off # disable screen saver
xset s noblank # don't blank the video device
#sleep 25s
#midori -e Fullscreen -a http://monitoring.hilark.int
#midori -a http://10.9.0.6
/usr/bin/chromium-browser --start-fullscreen monitoring.hilark.int
