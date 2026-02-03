# windows-ricing
### windows ricing - customization of windows appearance and behavior, closer to linux.

### project goal
make windows customization similar to linux, providing convenient window management and application autostart.

---

### versions of readme in other languages:
- [english](README.md)
- [русский](README.ru.md)
- [eesti](README.et.md)

---

# preview

![l](images/img1.jpg)
![o](images/img2.jpg)
![l](images/img3.jpg)

---

## 1. glazewm

#### glazewm is a window manager for windows. it automatically arranges windows based on code.

this project uses a config from the original glazewm repository with minor changes, namely changing the border color to pink, making inactive windows more transparent, and adding new hotkeys.

---

#### installing glazewm

go to this repository:
https://github.com/glzr-io/glazewm

click releases on the right and download the appropriate version.

i used: v3.9.1 Standalone Installer (x64)

zebar is also required for work:
https://github.com/glzr-io/zebar

i used: v3.2.0 Installer (Windows x64)

---

### interface changes

1. run zebar as administrator.
2. run glazewm as administrator.
3. glazewm should appear in the system tray.
if it doesn't appear there, go to your computer settings - personalization - taskbar, find "other taskbar icons" and turn on glazewm.
4. right-click on glazewm in the system tray, then "show config folder".
5. copy the code from my glazewm/config.yaml and replace it in your config, which was automatically downloaded with glazewm.
6. save and then press alt+shift+r - changes should apply automatically.

---

## 2. autostart on pc startup

if you skip this step, glazewm won't work after a reboot until you run it as administrator again. to avoid repeating the same action every time the pc starts, do the following:

install python: https://www.python.org/downloads/

save my autostart.py code, then open cmd as administrator and enter the command:

```
schtasks /create /tn "autostart_glazewm" /tr "C:\Program Files\glzr.io\GlazeWM\glazewm.exe" /sc onlogon /rl highest /f

```

we run it through cmd so the code executes with highest privileges; if you run the code through, for example, visual studio, it won't work.

go to task scheduler and find the autostart_glazewm task; if you see it, then everything is done correctly and working.

---

### if something is not working, possible problems:

1. wrong path to glazewm in the cmd command and autostart.py. check the path where your glazewm.exe is downloaded, and if the path differs from mine, change it in the second line of my code and then in the cmd command.
2. antivirus is blocking autostart. disable antivirus temporarily.
3. python is not running. run the python file and answer y to all questions in the console. if you have problems installing python, find any tutorial on youtube and install python according to their instructions.
