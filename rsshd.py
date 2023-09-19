#!/usr/bin/python3

## Autor: Pedro Flor
## Version: 0.3

## Usar dentro de "tmux"

import socket
import time
import logging
import subprocess
import os

PORT = 5522
SERVER="IP-VPS"
SLEEP = 5
USER = "support"
### SSH Command: 
# ssh -C -N -R 5544:localhost:22 -o ServerAliveInterval=60 -o ServerAliveCountMax=2592000 user-VPS@IP-VPS
#  -C => Compression
#  -N => Do not execute a remote command. Useful for just forwarding ports.
#  -R => Reverse tunnel
COMMAND = ["ssh", "-C", "-N", "-R", str(PORT) + ":localhost:" + "22", "-o", "ServerAliveInterval=60", "-o", "ServerAliveCountMax=2592000" , USER + "@" + SERVER]
LOG_PATH = "/tmp/rsshd.log"

def isOpen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(SLEEP)
    try:
        s.connect((ip, int(port)))
        return True
    except:
        return False

def daemon():
    while True:
        if isOpen(SERVER, PORT) == False:
            log_to_file("No existe SSH reverso activo")
            try:
                log_to_file("Iniciando SSH reverso")
                subprocess.run(COMMAND, 
                               shell=False,
                               capture_output=True)
            except:
                log_to_file("No fue posible iniciar SSH reverso")
        time.sleep(SLEEP)

def log_to_file(msg):
    logging.basicConfig(filename=LOG_PATH, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p', filemode='a')
    logging.warning(msg)

def banner():
    banner = "" + \
        " _____ _____ _____    _____                 _ \n" + \
        "|   __|   __|  |  |  |_   _|_ _ ___ ___ ___| |\n" + \
        "|__   |__   |     |    | | | | |   |   | -_| |\n" + \
        "|_____|_____|__|__|    |_| |___|_|_|_|_|___|_|"
    print(banner)

def check_tmux():
    banner = "" + \
        "                E R R O R !!! \n" + \
        "________  __       __  __    __  __    __ \n" + \
        "$$$$$$$$\ $$\      $$\ $$\   $$\ $$\   $$\  \n" + \
        "\__$$  __|$$$\    $$$ |$$ |  $$ |$$ |  $$ | \n" + \
        "   $$ |   $$$$\  $$$$ |$$ |  $$ |\$$\ $$  | \n" + \
        "   $$ |   $$\$$\$$ $$ |$$ |  $$ | \$$$$  /  \n" + \
        "   $$ |   $$ \$$$  $$ |$$ |  $$ | $$  $$<   \n" + \
        "   $$ |   $$ |\$  /$$ |$$ |  $$ |$$  /\$$\  \n" + \
        "   $$ |   $$ | \_/ $$ |\$$$$$$  |$$ /  $$ | \n" + \
        "   \__|   \__|     \__| \______/ \__|  \__| \n" + \
        "\n" + \
        "             EJECUTAR TMUX!!! \n" + \
        ""
    
    try:
        os.environ['TMUX']
    except:
        print(banner)
        exit(1)

if __name__ == "__main__":
    os.system("clear")
    check_tmux()
    banner()
    daemon()
