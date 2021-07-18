# Install "Debian Testing" minimal

# Convert Debian minimal to Kali
apt -y install wget gnupg dirmngr
wget -q -O - https://archive.kali.org/archive-key.asc | gpg --import
gpg --keyserver keyserver.ubuntu.com --recv-key 44C6513A8E4FB3D30875F758ED444FF07D8D0BF6
echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list
### OPCIONAL 
### echo "deb http://http.kali.org/kali kali-last-snapshot main non-free contrib" >> /etc/apt/sources.list
gpg -a --export ED444FF07D8D0BF6 | apt-key add -

# Editar sources.list y dejar únicamente Kali Repos
vi /etc/apt/sources.list

# Actualizar paquetes usando repositorio Kali
apt -y update && apt -y upgrade
apt -y dist-upgrade
apt -y autoremove --purge

# Instalar software base
apt -y install vim tmux bash-completion rlfe nmap ncat sudo mlocate net-tools curl unzip htop

# Swith to runlevel 3
systemctl isolate multi-user.target
systemctl set-default multi-user.target

# Stop firewall
systemctl stop ufw
systemctl disable ufw

# Instalar software adicional (Revisar Google Docs)
