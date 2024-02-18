#!/bin/bash


## Install software

rm /usr/lib/python3.11/EXTERNALLY-MANAGED
rm /usr/lib/python3.12/EXTERNALLY-MANAGED
apt -y install autoconf automake bash build-essential cmake curl git libcurl4 libssl-dev m4 make python3 python3-pip tmux vim wget nload bmon bwm-ng vnstat
cd
git clone https://github.com/MatrixTM/MHDDoS.git
cd MHDDoS
pip3 install -r requirements.txt --break-system-packages
pip3 install -r requirements.txt --break-system-packages


## Create user
useradd -m -s /bin/bash -p $(openssl passwd -1 AHINECDSgRnP0xFBhvq5) ddos
usermod -aG sudo ddos

# Final setup
mv /root/MHDDoS/ /home/ddos
chown -R ddos:ddos /home/ddos/MHDDoS
