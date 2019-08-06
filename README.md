# pcncserverscom
coomunicating pcnc servers using flask REST API

Before running and modifying code, install avahi-daemon (mdns service to get local domain name) and set the hostname of raspberry in local LAN network.

Steps:
1. sudo apt-get update
2. sudo apt-get install avahi-daemon
3. sudo /etc/init.d/avahi-daemon start
change hostname to pcnc1 or pcnc2 depending on machine
4. sudo gedit hostname
# change hostname in fornt of 127.0.1.1 to pcnc1 or pcnc2
# reboot the system to reflect changes.
5. sudo reboot
#
6. sudo /etc/init.d/avahi-daemon start
# clone the code from git.
7. git clone https://github.com/sahilgupta221/pcncserverscom.git
8. cd pcncserverscom/flaskpcnccom/
# open a new terminal tab with same location.
9 run hello-flask.py on window 1 and clientapihit.py on window 2.
10. modify code as per requirement.
