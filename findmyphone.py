import time
from bt_proximity import BluetoothRSSI #View readme for the prerequisites to run this.

phone = '' #Bluetooth MAC address of phone
dur = 6
newavg = 0
def get_signal_stength(mac):
    avg = 0
    for i in range(0, dur):
        time.sleep(0.2)
        b = BluetoothRSSI(mac)
        print(b.get_rssi())
        avg = avg + b.get_rssi()
    global newavg
    newavg = avg / dur

get_signal_stength(phone)
print('Average is ', newavg)
