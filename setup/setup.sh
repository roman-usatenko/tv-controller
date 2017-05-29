#!/usr/bin/env bash
# Manual pre steps are:
# 1. enable SSH
# 2. enable lirc module in  /boot/config.txt : dtoverlay=lirc-rpi,gpio_out_pin=17
# 3. apt-get -y install git && git clone https://github.com/roman-usatenko/tv-controller.git && cd tv-controller
apt-get -y update
apt-get -y upgrade
apt-get -y install supervisor lirc python-pip
pip -y install flask
cp hardware.conf /etc/lirc/
cp lircd.conf /etc/lirc/
