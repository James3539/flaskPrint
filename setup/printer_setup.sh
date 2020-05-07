

#!/bin/bash
cd ~
sudo git clone https://github.com/James3539/flaskPrint.git
cd flaskPrint

sudo apt -y  update
sudo apt -y  full-upgrade
sudo apt-get -y install nginx
sudo apt-get -y install python3-pip
sudo apt-get -y install wkhtmltopdf

sudo apt-get -y install cups
sudo apt-get -y install libcups2-dev

sudo apt-get -y install wget git-core

sudo pip3 install flask uwsgi
sudo pip3 install flask-api
sudo pip3 install Pillow
sudo pip3 install imgkit
sudo pip3 install pycups
sudo pip3 install beautifulsoup4

cd ~
mkdir downloads
cd downloads
sudo  wget 'http://www.argox.com/wp-content/uploads/largedriver/ARGOX_RPi_Printer_Driver-V1.5.0(armhf).tar.gz'
tar -xvzf "ARGOX_RPi_Printer_Driver-V1.5.0(armhf).tar.gz"
cd 'ARGOX_RPi_Printer_Driver-V1.5.0(armhf)'
sudo ./install


cd ~
sudo git clone https://github.com/James3539/flaskPrint.git
sudo chown www-data /home/pi/flaskPrint
sudo cp flaskPrint/setup/rc.local  /etc/rc.local
sudo rm /etc/nginx/sites-enabled/default
sudo cp flaskPrint/setup/flaskPrint_proxy   /etc/nginx/sites-available/flaskPrint_proxy
sudo ln -s /etc/nginx/sites-available/flaskPrint_proxy /etc/nginx/sites-enabled

sudo service nginx restart






