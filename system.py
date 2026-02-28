
import shlex
import subprocess
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import psutil

PING_CMD = ["ping", "-c", "2", "google.com"]
kernel = "pacman -S linux-zen linux-zen-firmware"
desktop = "pacman -S plasma-desktop kitty"
laptop = "pacman -S gnome tcp kitty"
locals = "loadkeys ru && setfont ter-c32b"


def check_internet(self):
    try:
        r = subprocess.run(PING_CMD, capture_output=True)
        return r.returncode == 0
    except Exception:
        return False

def install_kernel(self):
    try:
        linux = subprocess.run(shlex.split(kernel), capture_output=True)
        return linux.returncode == 0
    except Exception:
        return False

def desk(self):
    try:
        kde = subprocess.run(shlex.split(desktop), capture_output=True)
        return kde.returncode == 0
    except Exception:
        return False

def lapt (self):
    try:
        gnome = subprocess.run(shlex.split(laptop), capture_output=True)
        return gnome.returncode == 0
    except Exception:
        return False

def loc(self):
    try:
        local = subprocess.run(shlex.split(locals), capture_output=True)
        return local.returncode == 0
    except Exception:
        return False


def get_disks():
    disks = []

    for part in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(part.mountpoint)
        except PermissionError:
            continue

        disks.append({
            "device": part.device,
            "mount": part.mountpoint,
            "total": usage.total,
            "used": usage.used,
            "free": usage.free
        })

    return disks

