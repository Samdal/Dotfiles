# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty -e fish"                             # My terminal of choice
myConfig = "/home/halvard/.config/qtile/config.py"    # The Qtile config file location

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "d",
             lazy.spawn("dmenu_run -p 'Run: '"),
             desc='Dmenu Run Launcher'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod,], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift", "control"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod], "a",
             lazy.spawn("emacs"),
             desc='Start Emacs'
             ),
         Key([mod, "shift"], "w",
             lazy.spawn("firefox"),
             desc='Start Firefox'
             ),
         Key([mod], "v",
             lazy.spawn("virt-manager"),
             desc='Start virt-manager'
             ),
         Key([mod, "shift"], "e",
             lazy.spawn("thunar"),
             desc='Start thunar'
             ),
         Key([mod, "shift"], "d",
             lazy.spawn("discord"),
             desc='Start Discord'
             ),
         Key([mod, "shift"], "s",
             lazy.spawn("flameshot gui"),
             desc='Take screenshot'
             ),
         Key([mod], "s",
             lazy.spawn("steam"),
             desc='Start Steam'
             ),
         Key([mod], "g",
             lazy.spawn("gimp"),
             desc='Start Gimp'
             ),
         Key([mod, "shift"], "g",
             lazy.spawn("godot"),
             desc='Start Godot'
             ),
         Key([mod], "b",
             lazy.spawn("krita"),
             desc='Start Krita'
             ),
         Key([mod], "p",
             lazy.spawn("pavucontrol"),
             desc='Start pavucontrol'
             ),
         Key([mod, "shift"], "p",
             lazy.spawn("pulseeffects"),
             desc='Start pulseeffects'
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([mod], "r",
             lazy.to_screen(2),
             desc='Keyboard focus to monitor 3'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Window controls
         Key([mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod, "shift"], "m",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
]

group_names = [
    ("1", {'layout': 'monadtall'}),
    ("2", {'layout': 'monadtall'}),
    ("3", {'layout': 'monadwide'}),
    ("4", {'layout': 'monadtall'}),
    ("5", {'layout': 'monadtall'}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 1,
                "margin": 5, 
                "border_focus": "fabd2f",
                "border_normal": "282828"
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.MonadWide(**layout_theme),
]

colors = [["#282828", "#282828"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ebdbb2", "#ebdbb2"], # font color for group names
          ["#fabd2f", "#fabd2f"], # border line color for current tab
          ["#282828", "#282828"], # border line color for other tab and odd widgets
          ["#504946", "#504946"], # color for the even widgets
          ["#b8bb26", "#b8bb26"], # window name
          ["#b8bb26", "#b8bb26"]] # font 2

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="iosevka Medium",
    fontsize = 15,
    padding = 0,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.TaskList(
                       foreground = colors[6],
                       background = colors[0],
                       ),
              widget.Systray(
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       font="Hack Nerd Font",
                       background = colors[4],
                       foreground = colors[5],
                       padding = -5.5,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[5],
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[5],
                       format = '{MemUsed}MB',
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('gnome-system-monitor')},
                       measure_mem = 'G',
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       font="Hack Nerd Font",
                       background = colors[5],
                       foreground = colors[4],
                       padding = -5.5,
                       fontsize = 37
                       ),
              widget.TextBox(
                      text = "♪",
                       font="Hack Nerd Font",
                       foreground = colors[2],
                       background = colors[4],
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       font="Hack Nerd Font",
                       background = colors[4],
                       foreground = colors[5],
                       padding = -5.5,
                       fontsize = 37
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[5],
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       font="Hack Nerd Font",
                       background = colors[5],
                       foreground = colors[4],
                       padding = -5.5,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[4],
                       format = "%A, %B %d | %H:%M",
                       padding = 5
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
