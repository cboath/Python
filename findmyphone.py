import time
from bt_proximity import BluetoothRSSI #View readme for the prerequisites to run this.

phone = '' #Bluetooth MAC address of phone

def get_signal_stength(mac):
    while(True):
        time.sleep(0.2)
        b = BluetoothRSSI(mac)
        print(b.get_rssi())

get_signal_stength(phone)