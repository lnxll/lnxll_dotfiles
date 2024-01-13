import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

@hook.subscribe.startup_once
def autostart_once():
    home = os.path.expanduser('~/.config/qtile/autostart_once.sh')  # path to my script, under my user directory
    subprocess.call([home])

@hook.subscribe.startup
def autostart():
    subprocess.call("nitrogen --set-zoom-fill --random ~/.wallpaper/ --save",shell=True)

mod = "mod4"
terminal = "alacritty"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.group.next_window(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "m", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),

    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "q", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc="menu shutdown"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn("pycharm"), desc="Launch pycharm"),

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc='brightness Down'),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume +5"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -5"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([mod], "b", lazy.hide_show_bar(), desc="Hides the bar"),
    Key([mod], "z", lazy.window.bring_to_front(), desc='up window'),
]

groups = [Group(f"{i + 1}", label="󰏃") for i in range(8)]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Columns(margin=[30, 30, 30, 30],
                   border_focus_stack="#d75f5f",
                   border_width=3,
                   ),
    layout.Columns(margin=[10, 10, 10, 10],
                   border_focus_stack="#FF0000",
                   border_width=3,
                   ),
    layout.Max(),
    ]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=15,
                    background='#282738',
                ),
                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1":power},
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),

                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active='#CAA9E0',
                    block_highlight_text_color="#91B1F0",
                    highlight_color='#4B427E',
                    inactive='#282738',
                    foreground='#4B427E',
                    background='#353446',
                    this_current_screen_border='#353446',
                    this_screen_border='#353446',
                    other_current_screen_border='#353446',
                    other_screen_border='#353446',
                    urgent_border='#353446',
                    rounded=True,
                    disable_drag=True,
                ),

                widget.Spacer(
                    length=8,
                    background='#353446',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background="#353446"
                ),

                widget.CurrentLayout(
                    background='#353446',
                    foreground='#CAA9E0',
                    fmt='{}',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1": search},
                ),

                widget.TextBox(
                    fmt='Search',
                    background='#282738',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground='#CAA9E0',
                    mouse_callbacks={"Button1": search},
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),

                widget.WindowName(
                    background='#353446',
                    format="{name}",
                    font='JetBrains Mono Bold',
                    foreground='#CAA9E0',
                    empty_group_string='Desktop',
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),

                widget.Systray(
                    background='#282738',
                    fontsize=2,
                ),

                widget.TextBox(
                    text=' ',
                    background='#282738',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background='#353446',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background='#353446',
                ),

                widget.Spacer(
                    length=-7,
                    background='#353446',
                ),

                widget.Memory(
                    background='#353446',
                    format='{MemUsed: .0f}{mm}',
                    foreground='#CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#353446',
                ),

                widget.Backlight(
                    background='#353446',
                    backlight_name='amdgpu_bl2',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground='#CAA9E0',
                    fmt="*{}",
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#353446',
                ),

                widget.BatteryIcon(
                    theme_path='~/.config/qtile/Assets/Battery/',
                    background='#353446',
                    scale=1,
                ),

                widget.Battery(
                    font='JetBrains Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    format='{percent:2.0%}',
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#353446',
                ),

                widget.Volume(
                    font='JetBrainsMono Nerd Font',
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    fontsize=13,
                    background='#353446',
                ),

                widget.Spacer(
                    length=-5,
                    background='#353446',
                ),

                widget.Volume(
                    font='JetBrains Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background='#353446',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background='#282738',
                    margin_y=6,
                    margin_x=5,
                ),

                widget.Clock(
                    format='%H:%M %p',
                    background='#282738',
                    foreground='#CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),

                widget.Spacer(length=18, background='#282738'),
            ],
            30,
            border_color='#282738',
            border_width=[0, 0, 0, 0],
            margin=[12, 8, 4, 8],
        ),
        x11_drag_polling_rate=60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
