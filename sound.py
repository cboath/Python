#sudo apt-get install sox
import os
duration = 1
freq = 400
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
