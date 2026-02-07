import time
import sys
from src import pakages
from src import confsettings
from src import app  

class ProcessStarter:
    def __init__(self):
        self.ascii_intro = "Welcome To Installer TokyoHimura"

    def start_sync(self):
        print(self.ascii_intro)
        time.sleep(1)

        if pakages.select_lang(): 
            print("\n[STEP 1] Packages installed successfully.")
        else:
            print("\n[ERROR] Package installation failed or cancelled.")
            return

        print("\n[STEP 2] Starting configuration setup...")
        if confsettings.fileconfig():
            print("[OK] Configs applied.")
        else:
            print("[ERROR] Failed to move config files.")
            return

        print("\n[STEP 3] Launching TokyoHimura Dashboard...")
        self.launch_gui()

    def launch_gui(self):
        app.run_gui() 

if __name__ == "__main__":
    starter = ProcessStarter()
    starter.start_sync()