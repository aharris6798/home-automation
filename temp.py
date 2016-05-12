import glob
import os
import time

class Temp18B20:
    
    def __int__(self, gpio_object):
        self.__board = gpio_object
        self.__base_dir = '/sys/bus/w1/devices/'
        self.__device_folder = glob.glob(self.__base.dir + '28*')[0]
        self.__device_file = self.__device_folder + '/w1_slave'

        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

    
    @property
    def C(self):
        return self.__read_temp()[0]

    @property
    def F(self):
        return self.__read_temp()[1]

    def __read_temp_raw(self):
        f = open(self.__device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
 
    def __read_temp(self):
        lines = self.__read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.__read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f


if __name__ == '__main__':
    from board import Board

    rpi = Board()
    temp_sensor = Temp18B20(rpi)
    print('Temperature = ' + str(int(temp_sensor.C)) + ' degrees celcius')
