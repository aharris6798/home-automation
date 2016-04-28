class RGB_Led:
    def __init__(self, gpio_object, r, g, b, pwm = False):
        self.__pwm = pwm
        self.__red_pin = r
        self.__green_pin = g
        self.__blue_pin = b
        self.outputs = [self.__red_pin, self.__green_pin, self.__blue_pin]
        self.__board = gpio_object

        self.__setup_pins()

    def __setup_pins(self):
        if not self.__pwm:
            for pin in self.outputs:
                self.__board.GPIO.setup(pin, self.__board.GPIO.OUT)
        elif self.__pwm:
            print('DEBUG')
            
        else:
            print('Error try again')
        
    def red_turnon(self):
        ''' Turn's on red led '''
        self.off()
        self.__board.GPIO.output(self.__red_pin, self.__board.GPIO.HIGH)

    def green_turnon(self):
        ''' Turn's on green led '''
        self.off()
        self.__board.GPIO.output(self.__green_pin, self.__board.GPIO.HIGH)

    def blue_turnon(self):
        self.off()
        ''' Turn's on blue led '''
        self.__board.GPIO.output(self.__blue_pin, self.__board.GPIO.HIGH)

    def off(self):
        ''' Turn's all LEDs off '''
        for pin in self.outputs:
            self.__board.GPIO.output(pin, self.__board.GPIO.LOW)

if __name__ == "__main__":
    from board import Board    
    from time import sleep
    B = Board()
    led = RGB_Led(B, 26, 19, 13)

    led.red_turnon()
    sleep(1)
    led.off()
    led.green_turnon()
    sleep(1)
    led.off()
    led.blue_turnon()
    sleep(1)
    led.off()
