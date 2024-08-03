#!/bin/bash

## Autor: Pedro Flor
## Version: 1.1

# Variables

LPORT=30100       # Port to open on remote SSH server
RHOST="vultr"     # IP/Hostname of remote SSH server
RPORT=22          # SSH port on local SSH server (By default: TCP/22)
RPORT_VPS=22      # Remote SSH port on remote SSH server (By default: TCP/22)
RUSER="tunnel"    # Usuario en VPN "SIN" shell real -> /bin/false
WAIT_RECONN=5     # Minutes to wait to reconnect SSH

# -f              # Background. Evita que se cierre la sesión, aún si la shell parent muere.

#export AUTOSSH_LOGFILE=/tmp/autossh.log     # PATH for log file
export AUTOSSH_GATETIME=0                   # Intentar reconectar indefinidamente # Espera 60 segundos antes de considerar un fallo como permanente al inicio.
export AUTOSSH_MAXLIFETIME=900              # Reinicia la conexión cada 15 minutos.
export AUTOSSH_POLL=60                      # Verifica el estado de la conexión cada 60 segundos.
export AUTOSSH_FIRST_POLL=30                # Realiza la primera verificación 30 segundos después de establecer la conexión.


function logging_ssh_tunnel() {
    # TODO
    echo ""
}

function check_tmux() {

    IS_TMUX=$(env | grep 'TERM_PROGRAM=' | cut -f2 -d'=')

    if [ -z ${IS_TMUX} ] || [ ${IS_TMUX} != "tmux" ]
    then
        echo '
                        E R R O R !!!
        ________  __       __  __    __  __    __
        $$$$$$$$\ $$\      $$\ $$\   $$\ $$\   $$\
        \__$$  __|$$$\    $$$ |$$ |  $$ |$$ |  $$ |
           $$ |   $$$$\  $$$$ |$$ |  $$ |\$$\ $$  |
           $$ |   $$\$$\$$ $$ |$$ |  $$ | \$$$$  /
           $$ |   $$ \$$$  $$ |$$ |  $$ | $$  $$<
           $$ |   $$ |\$  /$$ |$$ |  $$ |$$  /\$$\
           $$ |   $$ | \_/ $$ |\$$$$$$  |$$ /  $$ |
           \__|   \__|     \__| \______/ \__|  \__|

                     EJECUTAR TMUX!!!
        '
        exit
    fi
}

function ssh_daemon() {
    while true
    do
        echo "Starting 'autossh' on "$(date)
        autossh -M 0 -C -N -R ${LPORT}:localhost:${RPORT} -o ServerAliveInterval=60 -o ServerAliveCountMax=2592000 -o ExitOnForwardFailure=yes ${RUSER}@${RHOST} -p ${RPORT_VPS}
        sleep ${WAIT_RECONN}m
    done
}



## Main
check_tmux
ssh_daemon
