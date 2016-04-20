import board from Board
import led from Led

rpi = Board()
led1 = Led(rpi,11 )
led1.turn_on()
led1.turn_off()
