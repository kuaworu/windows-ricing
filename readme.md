# windows-ricing
### windows ricing - customization of windows appearance and behavior, closer to linux.

### project goal
make windows customization similar to linux, providing convenient window management and application autostart.

---

# preview

<img width="600" alt="изображение" src="https://github.com/user-attachments/assets/4ea136a4-393b-483a-ac2c-a1cedf6df153" />
<img width="600" alt="изображение" src="https://github.com/user-attachments/assets/a896fac9-fc94-4718-aad2-a1ee94397e74" />
<img width="600" alt="изображение" src="https://github.com/user-attachments/assets/5b217dc3-f1ee-4e7e-a342-c985d27ad0cf" />
<img width="600" alt="изображение" src="https://github.com/user-attachments/assets/cc375360-8069-4197-8369-aeb0f6190e3a" />
<img width="600" alt="изображение" src="https://github.com/user-attachments/assets/8894a473-9168-405a-80f5-fb1d1ca2a469" />
<img width="600" alt="изображение" src="https://github.com/user-attachments/assets/d4396a08-9a37-4870-b5ea-3e6aecba6432" />
<img width="600" alt="изображение" src="https://github.com/user-attachments/assets/a5b2e5fa-8c96-4e81-93fd-43d329db524f" />

---

# table of contents

- [1. glazewm](#1-glazewm)
- [2. autostart on pc startup](#2-autostart-on-pc-startup)
- [3. taskbar](#3-taskbar)

---

## 1. glazewm

#### glazewm is a window manager for windows. it automatically arranges windows based on code.

this project uses a config from the original glazewm repository with minor changes.

---

### installing

go to this repository:
[glazewm](https://github.com/glzr-io/glazewm)

click releases on the right and download the appropriate version.

i used: v3.9.1 Standalone Installer (x64)

zebar is also required for work:
[zebar](https://github.com/glzr-io/zebar)

i used: v3.2.0 Installer (Windows x64)

yasb is also required for work:
[yasb](https://github.com/amnweb/yasb)

i used: yasb-2.0.5-x64.msi

yasb and zebar are utilities for taskbar customization, like the top taskbar in my screenshots for example. take your pick, i personally went with yasb.

---

### interface changes

1. run zebar or yasb as administrator.
2. run glazewm as administrator.
3. glazewm should appear in the system tray.
if it doesn't appear there, go to your computer settings - personalization - taskbar, find "other taskbar icons" and turn on glazewm.
4. right-click on glazewm in the system tray, then "show config folder".
5. copy the code from my `glazewm/config.yaml` and replace it in your config, which was automatically downloaded with glazewm.
6. save and then press `alt+shift+r` - changes should apply automatically.
7. also copy `yasb/config.yaml` and `yasb/styles.css` from my project into your yasb config and styles. if you are using zebar, i don't have the taskbar code that fits your setup, but you can find something similar on github or run any config that the app itself offers you.

---

## 2. autostart on pc startup

if you skip this step, glazewm won't work after a reboot until you run it as administrator again. to avoid repeating the same action every time the pc starts, do the following:

install python: [python](https://www.python.org/downloads/)

save my autostart.py code, then open cmd as administrator and enter the command:

```
schtasks /create /tn "autostart_glazewm" /tr "C:\Program Files\glzr.io\GlazeWM\glazewm.exe" /sc onlogon /rl highest /f

```

we run it through cmd so the code executes with highest privileges; if you run the code through, for example, visual studio, it won't work.

go to task scheduler and find the autostart_glazewm task; if you see it, then everything is done correctly and working.

---

## 3. taskbar

you need to download windhawk: [windhawk](https://windhawk.net/)

in the program, you need to enable the following modifications

<img width="600" alt="изображение" src="https://github.com/user-attachments/assets/e9917aac-130c-4067-807f-05a57b24d660" />

the configuration for each modification can be found in my repository at `windhawk/taskbar.txt`

not all modifications may work immediately for you. you might need to restart your pc.
