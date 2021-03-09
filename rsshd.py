#!/usr/bin/python3

## Autor: Pedro Flor
## Version: 0.2

## Usar dentro de "tmux"

import socket
import time
import logging
import subprocess
import os

PORT = 2221
SERVER="1.2.3.4"
SLEEP = 2
USER = "pf"
DAYS = 3
COMMAND = ["ssh", "-N", "-R", str(PORT) + ":localhost:" + "22", "-o", "ServerAliveInterval=60", "-o", "ServerAliveCountMax=" + str(DAYS*24*60), USER + "@" + SERVER]
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
        time.sleep(SLEEP)
        if isOpen(SERVER, PORT) == False:
            log_to_file("No existe SSH reverso activo")
            try:
                log_to_file("Iniciando SSH reverso")
                subprocess.run(COMMAND, 
                               shell=False,
                               capture_output=True)
            except:
                log_to_file("No fue posible iniciar SSH reverso")
                

def log_to_file(msg):
    logging.basicConfig(filename=LOG_PATH, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
    logging.warning(msg)

def banner():
    banner = "" + \
        "____ ____ _  _ ____ ____ ____ ____    ____ ____ _  _ \n" + \
        "|__/ |___ |  | |___ |__/ [__  |___    [__  [__  |__| \n" + \
        "|  \ |___  \/  |___ |  \ ___] |___    ___] ___] |  | \n" + \
        "\n" + \
        "           No cierrar esta ventana!!!\n"
    print(banner)

def check_tmux():

    
    banner = "" + \
        "████████ ███    ███ ██    ██ ██   ██\n" + \
        "   ██    ████  ████ ██    ██  ██ ██ \n" + \
        "   ██    ██ ████ ██ ██    ██   ███  \n" + \
        "   ██    ██  ██  ██ ██    ██  ██ ██ \n" + \
        "   ██    ██      ██  ██████  ██   ██\n"
    
    try:
        os.environ['TMUX']
    except:
        print(banner)
        exit(1)

if __name__ == "__main__":
    os.system("clear")
    banner()
    check_tmux()
    daemon()
