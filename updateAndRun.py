# Python 3.9
# Author: Daniel Limas
# Name: updateAndRunApp.py
# Version: 1.2.0

# Devious script to
# pull from repository 
# build ts and restart
# nodejs app

import subprocess 
from sys import argv

class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    LIGHT_GRAY = "\033[0;37m"
    BLACK = "\033[0;30m"

class Flags:
    HELP = "--help"
    KILL = "--kill"

SSH_ORIGIN = "ADD YOUR OWN SSH ORIGIN HERE"
BRANCH_NAME = "ADD YOUR DEPLOY BRANCH HERE"
PULL_COMMAND = "git pull " + SSH_ORIGIN + " " + BRANCH_NAME
BUILD_COMMAND = "npm run build"
KILL_COMMAND = "npm run daemon:kill"
START_COMMAND = "npm run daemon:start"

APP_NOT_RUNNING = "ERROR: No hay aplicaciones corriendo."
APP_ALREADY_RUNNING = "ERROR: La aplicacion ya se esta ejecutando."
KILL_COMMAND_HINT = "Prueba a ejecutar el script con el argumento: " + Colors.GREEN + "--kill" 

def update_repository():
    subprocess.call(PULL_COMMAND, shell=True)
    return

def kill_apps(): 
    try:
        subprocess.check_call(KILL_COMMAND, shell=True)
    except subprocess.CalledProcessError:
        print("\n" + Colors.RED + APP_NOT_RUNNING + "\n" + Colors.LIGHT_GRAY)
        return
    finally:
        return

def build_app():
    subprocess.check_call(BUILD_COMMAND, shell=True)

def start_app():
    try:
        subprocess.check_call(START_COMMAND, shell=True)
    except subprocess.CalledProcessError:
        print("\n" + Colors.RED + APP_ALREADY_RUNNING + "\n" + Colors.LIGHT_GRAY)
        print(KILL_COMMAND_HINT + Colors.LIGHT_GRAY + "\n")
        return

def start_project(kill_flag=False): 
    update_repository()
    build_app()
    if (kill_flag):
        kill_apps()
    start_app()
    return

def get_help():
    # TODO: Write help section
    print("AYUDA!!! 🍩")
    pass
 
def get_number_args():
    number_of_arguments = argv.__len__()
    if number_of_arguments == 2:
        process_flag()
    elif number_of_arguments <= 2:
        start_project(kill_flag=False)
        return
    else:
        get_help() 
    return

def process_flag():
    filename, flag = argv
    if (flag == Flags.HELP):
        get_help()
        return
    if (flag == Flags.KILL):
        start_project(kill_flag=True)
        return 

def main():
    get_number_args()

if __name__ == "__main__":
    main()