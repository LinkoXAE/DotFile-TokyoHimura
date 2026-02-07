import os 
import sys
import time

import shutil

import random
import math
import json

import shutil
import os
import time

def force_update_config():
    source = os.path.join(os.getcwd(), "src", ".config")
    destination = os.path.expanduser("~/.config")

    print("\n[!] WARNING: This will REPLACE your existing .config folders!")
    print("\n[!] ВНИМАНИЕ: Это ЗАМЕНИТ ваши существующие папки .config!")
    confirm = input("Are you sure? [y/N]: ").lower().strip()

    if confirm == 'y':
        print("STARTING SETTINGS OVERWRITE...")
        time.sleep(2)
        if os.path.exists(source):
            for item in os.listdir(source):
                s = os.path.join(source, item)
                d = os.path.join(destination, item)
                if os.path.exists(d):
                    if os.path.isdir(d):
                        shutil.rmtree(d)
                    else:
                        os.remove(d) 
                
                if os.path.isdir(s):
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)
                
                print(f"[ OK ] Updated: {item}")
            
            print("\nSUCCESS: All configs replaced!")
        else:
            print(f"ERROR: Source {source} not found!")
    else:
        print("Operation cancelled. No files were changed.")


