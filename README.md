# pcncserverscom

Before running and modifying code, install avahi-daemon (mdns service to get local domain name) and set the hostname of raspberry in local LAN network.

Steps:
1. sudo apt-get update
2. sudo apt-get install avahi-daemon
3. sudo /etc/init.d/avahi-daemon start
change hostname to pcnc1 or pcnc2 depending on machine
4. sudo gedit hostname
#change hostname in fornt of 127.0.1.1 to pcnc1 or pcnc2
#install frenetic and pcnc from this link
5. https://github.com/uvm-plaid/pcnc

#reboot the system to reflect changes.
6. sudo reboot
7. sudo /etc/init.d/avahi-daemon start
#clone the code from git.
8. git clone https://github.com/sahilgupta221/pcncserverscom.git
9. cd pcncserverscom/flaskpcnccom/
#open a new terminal tab with same location.
10 run hello-flask.py on window 1 and clientapihit.py on window 2.
11. Modify code as per requirement.
