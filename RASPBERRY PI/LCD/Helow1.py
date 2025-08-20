import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 6
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22

lcd_columns = 16  # LCD Columns
lcd_rows = 2      # LCD Rows

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                   lcd_columns, lcd_rows)

        while True:
            lcd.message('HELLO\nWORLD!')
            time.sleep(6.0)
            lcd.clear()

            text = input("Enter String You Want To Display On Screen: ")
            lcd.message("HELLO")
            time.sleep(6.0)
            lcd.clear()

            lcd.message('RASPBERRY Pi')
            time.sleep(6.0)
            lcd.clear()

    except KeyboardInterrupt:
        destroy()
