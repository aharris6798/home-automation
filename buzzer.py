
class Buzzer:

    def __init__(self, gpio_object, buzpin):
        self._board = gpio_object
        self._buzpin = buzpin
        self._setup_buzzer()

    def _setup_buzzer(self):
        self._board.GPIO.setup(self._buzpin, self._board.GPIO.OUT)

    def buz_on(self):
        self._board.GPIO.output(self._buzpin, self._board.GPIO.HIGH)

    def buz_off(self):
        self._board.GPIO.output(self._buzpin, self._board.GPIO.LOW)

if __name__ == "__main__":
    from board import Board
    from time import sleep
    rpi = Board()
    buzzer = Buzzer(rpi, 24)
    buzzer.buz_on()
    sleep(2)
    buzzer.buz_off()
