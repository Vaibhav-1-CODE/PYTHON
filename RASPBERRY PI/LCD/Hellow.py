import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

#Raspberry Pi pin setup
lcd_rs=25
lcd_en=6
lcd_d4=23
lcd_d5=17
lcd_d6=18
lcd_d7=22

lcd_columns =16 #Define Ldc Columns and rows size foe=r 16*2 LCD
lcd_row=2
def destory():
          GPIO.cleanup()
if __name__ == '__main__' :
      try:
           while True:
           	          lcd=LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows)

           	          Lcd.message('HEllO \n WORLD !')
           	          time.sleep(6.0)
           	          lcd.clear()

           	          text=input("Emter String You Want To Dispaly On Screen  : ")
           	          time=sleep(6.0)
           	          lcd.clear()

           	          lcd.message('RASPBERRT Pi  ')
           	          time=sleep(6.0)

      except KeyboardInterrupt :
      	      destory()