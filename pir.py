import RPi.GPIO as gpio
import time

class Pir:
    def __init__(self, pirSensor, board, frame):
        self.frame = frame
        self.time = time
        self.board = board
        self.pirSensor = 32
        self.pirState = 0
        self.pirMethod()
    
    def pirMethod(self):
        for i in range(1, 7):
            self.pirState = self.board.input(self.pirSensor)
            time.sleep(0.25)
            if self.pirState == 1:
                self.pirState = 1
                return self.pirState
            elif self.pirState == 0:
                self.pirState = 0
            else:
                print('Error PIR not functioning, aborting...')
                self.board.cleanup()
                #sys.exit()
        self.pirState = str(self.pirState)
        return self.pirState

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    pirSensor = 18
    gpio.setup(pirSensor, gpio.IN)
    #p = Pir()
    for i in range(20):
        #p = Pir(pirSensor)
        pirState = gpio.input(pirSensor)
        print (pirState)
        time.sleep(0.3)
