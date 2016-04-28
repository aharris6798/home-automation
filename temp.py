import glob
import os
import time

class temp:
    
    def __int__(self, gpio_object):
    self.__board = gpio_object
    self.__base_dir = '/sys/bus/w1/devices/'
    self.__device_folder = glob.glob(self.__base.dir + '28*')[0]
    self.__device_file = self.__device_folder + '/w1_slave'

    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    
