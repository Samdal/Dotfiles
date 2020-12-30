#! /bin/bash 

#screen layout
sh ~/.screenlayout/layout.sh

picom &

#change keyboard layout and rebind caps lock to esc
setxkbmap -layout "no"
setxkbmap -option caps:escape

#audio from virutal machine
#scream -u -i enp4s0

#wacom tablet
xsetwacom --set "Wacom Intuos PT M 2 Pen stylus" MapToOutput 2560x1440+1920+240 &

#bluetooth
blueberry-tray

#wallpaper
sh /home/halvard/.config/qtile/slideshow.sh /home/halvard/Nextcloud/sync/bilder/ 5m &
