#!/bin/bash

# Author: Pedro Flor


function start_openvpn() {
    kill_sleep=3

    killall openvpn
    sleep $kill_sleep
    cd /home/pf/Documents/OpenVPN/PrivateVPN/TUNUDP/
    openvpn --daemon --config ./PrivateVPN-AR-BuenosAires-TUN-1194.ovpn
    sleep $kill_sleep
}

function check_openvpn() {

    
    GOOGLE_DNS="4.2.2.2"
    OpenVPN_IFACE="tun0"
    SLEEP="5s"
    WAIT_ICMP=2
    COUNT_ICMP=2

    while true
    do

        isOpenVPN_IFACE=$(ifconfig | grep ${OpenVPN_IFACE} | cut -f 1 -d":")
        ## Check if VPN Interface is UP (tun0)
        if [ -z $isOpenVPN_IFACE ]
        then
            echo "Restarting OpenVPN on" $(date) ":: Reason: Assuming no OpenVPN on ${OpenVPN_IFACE}." >> /tmp/openvpn-status-check.log
            start_openvpn
        else
           echo -n "."
        fi

        OpenVPN_GW=$(ip route | grep 0.0.0.0 | grep tun0 | cut -f3 -d" ")
        ## Check if VPN OpenVPN_GW is reachable
        if  [ ! -z "$(ping -I ${OpenVPN_IFACE} -q -c $COUNT_ICMP -W $WAIT_ICMP ${OpenVPN_GW} | grep '100% packet loss' )" ]
        then
            echo "Restarting OpenVPN on" $(date) ":: Reason: Can't ping to ${OpenVPN_GW} over ${OpenVPN_IFACE}." >> /tmp/openvpn-status-check.log
            start_openvpn
        else
           echo -n "."
        fi

        ## Check if GOOGLE_DNS is reachable
        if  [ ! -z "$(ping -I ${OpenVPN_IFACE} -q -c $COUNT_ICMP -W $WAIT_ICMP ${GOOGLE_DNS} | grep '100% packet loss' )" ]
        then
            echo "Restarting OpenVPN on" $(date) ":: Reason: Can't ping to ${GOOGLE_DNS} over ${OpenVPN_IFACE}." >> /tmp/openvpn-status-check.log
            start_openvpn
            
        else
           echo -n "."
        fi
        sleep $SLEEP
        echo -n "-"
    done
}

echo -n "Starting OpenVPN..."
start_openvpn

check_openvpn
