#! /bin/bash 

#screen layout
sh ~/.screenlayout/layout.sh

picom &

#change keyboard layout and rebind caps lock to esc
setxkbmap -layout "no"
setxkbmap -option caps:escape

#bluetooth
blueman-tray

#wallpaper
feh --bg-fill ~/Pictures/wallpapers/bs.jpg
