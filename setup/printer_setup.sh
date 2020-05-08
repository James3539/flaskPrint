
#!/bin/bash
cd ~
sudo apt -y  update
sudo apt -y  full-upgrade
sudo apt-get -y install git-core
sudo apt-get -y install nginx
sudo service nginx start
sudo apt-get -y install python3-pip
sudo apt-get -y install wkhtmltopdf
sudo apt-get install build-essential python-dev
sudo apt-get -y install cups
sudo apt-get -y install libcups2-dev

sudo pip3 install flask uwsgi flask-api Pillow imgkit beautifulsoup4 pycups

sudo git clone https://github.com/James3539/flaskPrint.git
sudo chown www-data /home/pi/flaskPrint
sudo cp /home/pi/flaskPrint/setup/rc.local  /etc/rc.local
sudo cp /home/pi/flaskPrint/setup/flaskPrint_proxy   /etc/nginx/sites-available/flaskPrint_proxy
sudo ln -s /etc/nginx/sites-available/flaskPrint_proxy /etc/nginx/sites-enabled

sudo service nginx restart

sudo usermod -a -G lpadmin pi
cd /home/pi
mkdir downloads
cd downloads
sudo  wget 'http://www.argox.com/wp-content/uploads/largedriver/ARGOX_RPi_Printer_Driver-V1.5.0(armhf).tar.gz'
tar -xvzf "ARGOX_RPi_Printer_Driver-V1.5.0(armhf).tar.gz"
cd 'ARGOX_RPi_Printer_Driver-V1.5.0(armhf)'
sudo ./install
sudo cp /home/pi/flaskPrint/setup/cupsd.conf /etc/cups/cupsd.conf







