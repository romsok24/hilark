#!/usr/bin/python3

# Ten prosty skrypt pomoga w przełączeniu 
# instncji Chromium kiosk-mode w full screen
# jesli odpowiedni przełącznik aplikacji nie zadziała

from evdev import uinput, ecodes as e

with uinput.UInput() as ui:
    #ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
    ui.write(e.EV_KEY, e.KEY_ESC, 1)
    ui.write(e.EV_KEY, e.KEY_F11, 1)
    ui.syn()
