#!/usr/bin/env bash
tty | grep tty > /dev/null
if [ $? -eq 0 ]; then
    cd /home/pi/tv-controller
    while true; do
        git pull
        #sudo openvt -e -f -c 1
        sudo python web.py
        echo Restarting....
        sleep 5
    done
fi
