import subprocess
path_glazewm = r"c:\program files\glzr.io\glazewm\glazewm.exe"
subprocess.run([
    "schtasks",
    "/create",
    "/tn", "autostart_glazewm",
    "/tr", path_glazewm,
    "/sc", "onlogon",
    "/rl", "highest",
    "/f"
],
check=True)
