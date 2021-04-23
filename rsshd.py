#!/usr/bin/python3

## Autor: Pedro Flor
## Version: 0.3

## Usar dentro de "tmux"

import socket
import time
import logging
import subprocess
import os

PORT = 2221
SERVER="127.0.0.1"
SLEEP = 2
USER = "pflor"
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
            log_to_file("No existe SSH reverso activo. Tratando de inicar SSH reverso...")
            try:
                #log_to_file("Tratando de inicar SSH reverso...")
                result = subprocess.run(COMMAND, 
                               shell=False,
                               capture_output=True)
                print(result.returncode)
                if result.returncode  == 0:
                    log_to_file("Se inicio exitosamente SSH reverso!!!")
                else:
                    log_to_file("No fue posible iniciar SSH reverso.")
            except:
                log_to_file("No fue posible iniciar SSH reverso.")
                

def log_to_file(msg):
    logging.basicConfig(filename=LOG_PATH, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')
    logging.warning(msg)

def banner_do_not_close():
    banner = "" + \
        "____ ____ _  _ ____ ____ ____ ____    ____ ____ _  _ \n" + \
        "|__/ |___ |  | |___ |__/ [__  |___    [__  [__  |__| \n" + \
        "|  \ |___  \/  |___ |  \ ___] |___    ___] ___] |  | \n" + \
        "\n" + \
        "           No cierrar esta ventana!!!\n"
    print(banner)

def banner_check_tmux():

    
    banner = "" + \
        "\n\n         Esta aplicacion requiere tmux!!!\n\n" + \
        "       ████████ ███    ███ ██    ██ ██   ██\n" + \
        "          ██    ████  ████ ██    ██  ██ ██ \n" + \
        "          ██    ██ ████ ██ ██    ██   ███  \n" + \
        "          ██    ██  ██  ██ ██    ██  ██ ██ \n" + \
        "          ██    ██      ██  ██████  ██   ██\n" + \
        "\n\n >>> Inicar sesion tmux y volver a intentarlo <<<\n"  + \
        "     ----------------------------------------\n"
    
    try:
        os.environ['TMUX']
    except:
        print(banner)
        exit(1)

if __name__ == "__main__":
    os.system("clear")
    banner_check_tmux()
    banner_do_not_close()
    daemon()
