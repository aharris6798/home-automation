
class RGB_Led: 
    def __init__(self, gpio_object, r, g, b, pwm = False):    
        self.__pwm = pwm
        self.__red.pin = r
        self.__green.pin = g
        self.__blue.pin = b
        self.outputs = [self.__red.pin, self.__green.pin, self.__blue.pin]
        self.__board = gpio_object


        self.__setup_pins(self):

    def __setup_pins()
        if not self.__pwm:
            for pin in self.outputs:
                self.__board.GPIO.setup(pin, self.__board.GPIO.OUT)
        elif self.__pwm:
            print('DEBUG: pwm')

        else:
            print('Error')

    def red_turnon(self):
        self.off()
        self.__board.GPIO.output(self.__red.pin, self.__board.GPIO.HIGH)

    def blue_turnon(self):
        self.off()
        self.__board.GPIO.output(self.__blue.pin, self.__board.GPIO.HIGH)

    def green_turnon(self):
        self.off()
        self.__board.GPIO.output(self.__green.pin, self.__board.GPIO.HIGH)

    def off(self):
        for pin in self outputs:
            self.__board.GPIO.output(pin, self.__board.GPIO.LOW)

if __name__ == "__main__":
    from board import Board    
    from time import sleep
    B = Board()
    led = RGB_Led(B, 26, 19 ,13)

    led.red_on()
    sleep(1)
    led.off()
    led.green_on()
    sleep(1)
    led.off()
    led.blue_on()
    sleep(1)
    led.off()             
