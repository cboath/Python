# Python

Dependencies install:
SENSORS AND CENTRAL COMPUTER: Bluetooth dependencies requirements

PREREQUISITES: Sudo -s apt-get update apt-get install python-pip libglib2.0 apt-get install python-dev pip install simplejson

BLUEZ INSTALL: apt-get install libdbus-1-dev libdbus-glib-1-dev libglib2.0-dev libical-dev libreadline-dev libudev-dev libusb-dev make mkdir -p work/bluepy cd work/bluepy wget https://www.kernel.org/pub/linux/bluetooth/bluez-5.32.tar.xz tar xvf bluez-5.32.tar.xz cd bluez-5.32 ./configure --disable-systemd make sudo make install (note this step can take a while)

BLUEPY INSTALL: pip install bluepy

PYBLUEZ INSTALL: Apt-get install libbluetooth-dev Apt-get install libboost-all-dev Apt-get install libcr-dev pip install pybluez pip install pybluez[ble]

git clone https://github.com/ewenchou/bluetooth-proximity.git cd bluetooth-proximity sudo python setup.py install



Stock suff needs API key update
Also needs pip install of alpha_vantage and pandas


Add water sensor and thermometer when can log back in.


HOCKEY:

sudo python3 src/main.py --led-gpio-mapping=adafruit-hat --led-brightness=60 --led-slowdown-gpio=2
