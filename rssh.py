#!/usr/bin/python3

## Autor: PiEf
## Version: 1.2

import socket
import time
import logging
import subprocess
import os
from datetime import datetime


LPORT = 20100       # Port to open on remote SSH server
RHOST = "vultr"     # IP/Hostname of remote SSH server
RPORT = 22          # Remote SSH port on remote SSH server (By default: TCP/22)
RPORT_VPS = 22      # Remote SSH port on remote SSH server (If not TCP/22)
RUSER = "tunnel"    # Usuario en VPN "SIN" shell real -> /bin/false
SECS_TEST_SOCKETS = 5   # Seconds to wait to test socket
SECS_RECONN_SSH = 5     # Seconds to wait to reconnect SSH


### SSH Command: 
# ssh -C -N -R 5544:localhost:22 -o ServerAliveInterval=60 -o ServerAliveCountMax=2592000 user-VPS@IP-VPS
#  -C => Compression
#  -N => Do not execute a remote command. Useful for just forwarding LPORTs.
#  -R => Reverse tunnel

#SSH_COMMAND_PROCESS = ["ssh", "-C", "-R", str(LPORT) + ":localhost:" + str(RPORT), "-o", "ServerAliveInterval=60", "-o", "ServerAliveCountMax=2592000" , RUSER + "@" + RHOST]
LOG_PATH = "/tmp/rssh.py.log"
MAX_FAILS = 3

def verify_socket(rhost, rport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((rhost, int(rport)))
        log_to_file("[Info]: Exito al establecer SOCKET TCP con el sistema remoto: <RHOST=" + rhost + ">" + " " + "<RPORT=" + str(rport)+">")
        return True
    except:
        print("[Error]: Imposible establecer SOCKET TCP con el sistema remoto: <RHOST=" + rhost + ">" + " " + "<RPORT=" + str(rport)+">")
        log_to_file("[Error]: Imposible establecer SOCKET TCP con el sistema remoto: <RHOST=" + rhost + ">" + " " + "<RPORT=" + str(rport)+">")
        return False


def create_ssh_tunnel(lport, rhost, rport, rport_vps):
    # Verify if the remote system is reachable
    if verify_socket(rhost, rport) == True:
        try:
            log_to_file("[Info]: Starting SSH tunnel: <LPORT=" + str(lport) + ">" + " " + "<RHOST=" + rhost + ">" + " " + "<RPORT=" + str(rport)+">" + "<RPORT_VPS=" + str(rport_vps)+">")
            # Starting process
            #subprocess.run(SSH_COMMAND_PROCESS, shell=False, capture_output=True)
            SSH_COMMAND_OS_SYSTEM = "ssh -C -N -R" + " " + str(lport) + ":localhost:22" + " " + "-o ServerAliveInterval=60 -o ServerAliveCountMax=2592000 -o ExitOnForwardFailure=yes" + " " + RUSER + "@" + rhost + " " + "-p" + " " + str(rport_vps)
            print("[Info]: Se procede a iniciar SSH reverso: <LPORT=" + str(lport) + ">" + " " + "<RHOST=" + rhost + ">" + " " + "<RPORT=" + str(rport)+">" + "<RPORT_VPS=" + str(rport_vps)+">")
            exit_status = os.system(SSH_COMMAND_OS_SYSTEM)
            return exit_status
        except:
            return 1
    else:
        time.sleep(SECS_TEST_SOCKETS)

def daemon_ssh():
    counter_fails = 0
    lport = LPORT
    rhost = RHOST
    rport = RPORT
    rport_vps = RPORT_VPS


    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    date_now = now.strftime("%d/%m/%Y %H:%M:%S")

    while True:
        if create_ssh_tunnel(lport, rhost, rport, rport_vps) != 0:
            counter_fails = counter_fails + 1
            log_to_file("[Error]: " + date_now + " No fue posible iniciar SSH reverso: <LPORT=" + str(lport) + ">" + " " + "<RHOST=" + rhost + ">" + " " + "<RPORT=" + str(rport)+">" + "<RPORT_VPS=" + str(rport_vps)+">")
            if counter_fails >= MAX_FAILS:
                lport += 1
                log_to_file("[Error]: " + date_now + " No fue posible iniciar SSH reverso: <LPORT=" + str(lport) + ">" + " " + "<RHOST=" + rhost + ">" + " " + "<RPORT=" + str(rport)+">" + "<RPORT_VPS=" + str(rport_vps)+">")
                create_ssh_tunnel(lport, rhost, rport, rport_vps)
                counter_fails = 0
        else:
            log_to_file("[Info]: " + date_now + " Se inicio SSH reverso exitosamente: <LPORT=" + str(lport) + ">" + " " + "<RHOST=" + rhost + ">" + " " + "<RPORT=" + str(rport)+">" + "<RPORT_VPS=" + str(rport_vps)+">")
        time.sleep(SECS_RECONN_SSH)

def log_to_file(msg):
    logging.basicConfig(filename=LOG_PATH, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p', filemode='a')
    logging.warning(msg)

def banner():
    banner = "" + \
        " _____ _____ _____    _____                 _ \n" + \
        "|   __|   __|  |  |  |_   _|_ _ ___ ___ ___| |\n" + \
        "|__   |__   |     |    | | | | |   |   | -_| |\n" + \
        "|_____|_____|__|__|    |_| |___|_|_|_|_|___|_|\n"
    print(banner)

def check_tmux():
    banner = "" + \
        "                E R R O R !!! \n" + \
        "________  __       __  __    __  __    __ \n" + \
        "$$$$$$$$\\ $$\\      $$\\ $$\\   $$\\ $$\\   $$\\  \n" + \
        "\\__$$  __|$$$\\    $$$ |$$ |  $$ |$$ |  $$ | \n" + \
        "   $$ |   $$$$\\  $$$$ |$$ |  $$ |\\$$\\ $$  | \n" + \
        "   $$ |   $$\\$$\\$$ $$ |$$ |  $$ | \\$$$$  /  \n" + \
        "   $$ |   $$ \\$$$  $$ |$$ |  $$ | $$  $$<   \n" + \
        "   $$ |   $$ |\\$  /$$ |$$ |  $$ |$$  /\\$$\\  \n" + \
        "   $$ |   $$ | \\_/ $$ |\\$$$$$$  |$$ /  $$ | \n" + \
        "   \\__|   \\__|     \\__| \\______\\/ \\__|  \\__| \n" + \
        "\n" + \
        "             EJECUTAR TMUX!!! \n" + \
        ""

    try:
        os.environ['TMUX']
    except:
        print(banner)
        exit(1)

if __name__ == "__main__":
    #os.system("clear")
    # Verify if TMUX is running
    check_tmux()
    banner()
    # Create SSH tunnel and profit!!!
    daemon_ssh()
    print("End....")
