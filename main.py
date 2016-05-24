from board import Board
from Led import Led
from temp2 import Temperature
from Rgb import RGB_Led
from LCD1602 import LCD1602
from time import sleep
from button import Button
from buzzer import Buzzer
from pir import Pir


rpi = Board()
led = Led(rpi,11)
rgb = RGB_Led(26, 19, 13)
button = Button(rpi, 27)
temp = Temperature()
lcd = LCD1602(rpi)
buzzer = Buzzer()
pir = Pir

while True:
    if
lcd.message()
