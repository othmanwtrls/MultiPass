import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

def afficher(donnee) :
	mylcd.lcd_clear()
        mylcd.lcd_display_string(donnee, 1)
        sleep(10)

def effacer():
	mylcd.lcd_clear()

