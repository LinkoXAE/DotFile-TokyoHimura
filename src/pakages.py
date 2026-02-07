import subprocess
import os
import webbrowser
import time

ascii_himura = r''' 
     ________   __  _   _ ________  ____   _______  ___  
    | ___ \ \ / / | | | |_   _|  \/  | | | | ___ \/ _ \ 
    | |_/ /\ V /  | |_| | | | | .  . | | | | |_/ / /_\ \
    | ___ \ \ /   |  _  | | | | |\/| | | | |    /|  _  |
    | |_/ / | |   | | | |_| |_| |  | | |_| | |\ \| | | |
    \____/  \_/   \_| |_/\___/\_|  |_/\___/\_| \_\_| |_/
'''

package = [
    "hyprland", "hyprlock", "cava", "fastfetch", "fish", "kitty", 
    "micro", "mousepad", "mpvpaper", "neofetch", "pipewire", 
    "pipewire-pulse", "waybar", "rofi-wayland", "thunar", 
    "wlogout", "xarchiver", "zathura"
]

def imitator_install(duration_seconds):
    bar = [" [=     ]", " [ =    ]", " [  =   ]", " [   =  ]", " [    = ]", " [     =]", " [    = ]", " [   =  ]", " [  =   ]", " [ =    ]"]
    end_time = time.time() + duration_seconds
    i = 0
    while time.time() < end_time:
        print(bar[i % len(bar)], end="\r")
        time.sleep(0.1)
        i += 1
    print(" [ DONE ]")

class InstallerPackage:
    def installpkg_eng(self):
        useraccept = input("Continue install package? [Y/n]: ")
        if useraccept.upper() in ["Y", "YES"]:
            print(ascii_himura)
            print("Preparing environment...")
            imitator_install(3) 
            print("\nInstall starting...")
            subprocess.run(["sudo", "pacman", "-S", "--needed"] + package)
            time(10)
            print("Install end")
        else:
            print("Installation cancelled.")

    def installpkg_rus(self):
        useraccepts = input("Продолжить установку пакетов? [Y/n]: ")
        if useraccepts.upper() in ["Y", "YES", "Д", "ДА"]:
            print(ascii_himura)
            print("Подготовка среды...")
            imitator_install(3)
            print("\nСкачивание началось...")
            subprocess.run(["sudo", "pacman", "-S", "--needed"] + package)
            time(10)
            print("Скачевание завершено")
        else:
            print("Скачивание отменено.")

def select_lang():
    print("\n1. Eng")
    print("2. Ru")
    print("0. Exit")
    selected = input("\n>>> ")

    installer = InstallerPackage()

    if selected == '1':
        installer.installpkg_eng()
    elif selected == '2':
        installer.installpkg_rus()
    else: 
        print("Exit..")

if __name__ == '__main__':
    select_lang()