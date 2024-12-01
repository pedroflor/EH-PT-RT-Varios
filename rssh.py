#!/usr/bin/python3

## Autor: PiEf
## Version: 1.3

from datetime import datetime
import grp
import logging
import os
import pwd
import socket
import stat
import subprocess
import time


LPORT = 20100               # Port to open on remote SSH server
RHOST = "216.215.215.216"   # IPv4 of remote SSH server (Important: Use IPv4 ONLY !!!)
RPORT = 22                  # Remote SSH port on remote SSH server (By default: TCP/22)
RPORT_VPS = 22              # Remote SSH port on remote SSH server (If not TCP/22)
RUSER = "tunnel_user"       # Usuario en VPN "SIN" shell real -> /bin/false
SECS_TEST_SOCKETS = 5       # Seconds to wait to test socket
SECS_RECONN_SSH = 5         # Seconds to wait to reconnect SSH
MAX_FAILS = 5
LOG_PATH = "/var/log/rssh.py.log"

#  -C => Compression
#  -N => Do not execute a remote command. Useful for just forwarding LPORTs.
#  -R => Reverse tunnel



def verify_socket(rhost, rport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((rhost, int(rport)))
        log_messages(f"[Info]: Remote SSH Server ready to accept SSH Tunnels: <RHOST={rhost}> <RPORT={str(rport)}>", LOG_PATH)
        return True
    except:
        log_messages(f"[Error]: Remote SSH Server unable accept SSH Tunnels: <RHOST={rhost}> <RPORT={str(rport)}>", LOG_PATH)
        return False


def create_ssh_tunnel(lport, rhost, rport, rport_vps):
    # Verify if the remote system is reachable
    if verify_socket(rhost, rport) == True:
        try:
            log_messages(f"[Info]: Starting SSH tunnel: <LPORT={str(lport)}> <RHOST={rhost}> <RPORT={str(rport)}> <RPORT_VPS={str(rport_vps)}>", LOG_PATH)
            # Starting process
            SSH_COMMAND_OS_SYSTEM = (f"ssh -C -N -R {str(lport)}:localhost:22 -o ServerAliveInterval=60 -o ServerAliveCountMax=2592000 -o ExitOnForwardFailure=yes {RUSER}@{rhost}  -p {str(rport_vps)}")
            exit_status = os.system(SSH_COMMAND_OS_SYSTEM)
            return exit_status
        except:
            return 1
    else:
        time.sleep(SECS_TEST_SOCKETS)
        return 1

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

    # Forever loop :)
    while True:
        create_ssh_tunnel_status_code = create_ssh_tunnel(lport, rhost, rport, rport_vps)
        if create_ssh_tunnel_status_code != 0:
            log_messages(f"[Error]: Exit status={create_ssh_tunnel_status_code}. Failed reverse SSH: <LPORT={str(lport)}> <RHOST={rhost}> <RPORT={str(rport)}> <RPORT_VPS={str(rport_vps)}>", LOG_PATH)
        else:
            log_messages(f"[Info]: Reverse SSH was successfully started: <LPORT={str(lport)}> <RHOST={rhost}> <RPORT={str(rport)}> <RPORT_VPS={str(rport_vps)}>", LOG_PATH)
        time.sleep(SECS_RECONN_SSH)

def log_messages(msg, log_file_path):

    # Verifica si el archivo existe
    if not os.path.exists(log_file_path):
        try:
            # Crear el archivo
            with open(log_file_path, "w") as log_file:
                log_file.write("")

            # Change permissions to 644
            os.chmod(log_file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

            # Change owner to tunnel:tunnel
            uid = pwd.getpwnam("tunnel").pw_uid
            gid = grp.getgrnam("tunnel").gr_gid
            os.chown(log_file_path, uid, gid)
        except PermissionError:
            print("Error: You do not have the necessary permissions to create or modify the file.")
        except FileNotFoundError:
            print("Error: Directory /var/log does not exist.")
        except KeyError:
            print("Error: User or group 'tunnel' does not exist.")
        except Exception as e:
            print(f"Unexpected Error: {e}")
    else:
        logging.basicConfig(filename=log_file_path, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p', filemode='a')
        logging.warning(msg)
        print(msg)

if __name__ == "__main__":
    try:
        # Create SSH tunnel and profit!!!
        daemon_ssh()
    except Exception as e:
        print(f"Unexpected Error: {e}")
