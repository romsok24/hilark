 #!/bin/sh
 
 # on raspbery pi you can run it from /etc/init.local
 
xset -dpms # disable DPMS (Energy Star) features.
xset s off # disable screen saver
xset s noblank # don't blank the video device
/usr/bin/chromium-browser --start-fullscreen --start-maximized --no-sandbox --kiosk http://www.onet.pl
#or another browser: midori -e Fullscreen -a http://www.onet.pl
