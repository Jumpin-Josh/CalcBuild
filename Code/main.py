import math
import time
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#LCD
I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(1, sda=machine.Pin(26), scl=machine.Pin(27), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#Debounces buttons
class Button:
    def __init__(self, pin_number, pull_up=True, debounce_delay=50, cooldown_delay=110):
        self._pull_up = pull_up
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP if pull_up else Pin.PULL_DOWN)
        self._last_state = self.read()  # Initialize with current state
        self._last_debounce_time = 0
        self._last_cooldown_time = 0
        self._debounce_delay = debounce_delay
        self._cooldown_delay = cooldown_delay

    def read(self):
        return self.pin.value() == (0 if self._pull_up else 1)

    def debounced_read_cooldown(self):
        current_state = self.read()
        current_time = time.ticks_ms()
        # Debounce
        if current_state != self._last_state:
            if current_time - self._last_debounce_time > self._debounce_delay:
                self._last_debounce_time = current_time
                self._last_state = current_state
        # Cooldown check
        if self._last_state and current_time - self._last_cooldown_time > self._cooldown_delay:
            if current_time - self._last_debounce_time > self._debounce_delay: #double check debounce.
                if self.read(): #final check to ensure still pressed.
                    self._last_cooldown_time = current_time
                    return True # button pressed and cooldown over
        if not self._last_state:
            self._last_cooldown_time = current_time # reset cooldown time if button is released.
        return False  # Button is not pressed, or cooldown is active.
    
#Button Assingment
p0 = Button(15)
p1 = Button(10)
p2 = Button(11)
p3 = Button(12)
p4 = Button(7)
p5 = Button(8)
p6 = Button(9)
p7 = Button(4)
p8 = Button(5)
p9 = Button(6)
cl = Button(13)
dec = Button(14)
enter = Button(16)
add = Button(17)
subt = Button(18)
mult = Button(19)
div = Button(20)
log = Button(2)
ln = Button(3)

#Variables
first = True
strnum1 = ''
strnum2 = ''
str_op = ''
log_op = False
ln_op = False

#Functions
def screenUpdate(num):
    global first, strnum1, strnum2, str_op, log_op, ln_op
    tempnum = ''
    
    #Numbers
    if(num == cl):
        lcd.clear()
        first = True
        strnum1 = ''
        strnum2 = ''
        str_op = ''
        log_op = False
        ln_op = False
    elif(num == p1):
        lcd.putchar('1')
        tempnum = '1'
    elif(num == p2):
        lcd.putchar('2')
        tempnum = '2'
    elif(num == p3):
        lcd.putchar('3')
        tempnum = '3'
    elif(num == p4):
        lcd.putchar('4')
        tempnum = '4'
    elif(num == p5):
        lcd.putchar('5')
        tempnum = '5'
    elif(num == p6):
        lcd.putchar('6')
        tempnum = '6'
    elif(num == p7):
        lcd.putchar('7')
        tempnum = '7'
    elif(num == p8):
        lcd.putchar('8')
        tempnum = '8'
    elif(num == p9):
        lcd.putchar('9')
        tempnum = '9'
    elif(num == p0):
        lcd.putchar('0')
        tempnum = '0'
    elif(num == dec):
        lcd.putchar('.')
        tempnum = '.'
    # Operations
    elif(num == add):
        lcd.putchar('+')
        first = False
        str_op = '+'
    elif(num == subt):
        lcd.putchar('-')
        first = False
        str_op = '-'
    elif(num == mult):
        lcd.putchar('*')
        first = False
        str_op = '*'
    elif(num == div):
        lcd.putchar('/')
        first = False
        str_op = '/'
    elif(num == log):
        lcd.putstr('log')
        log_op = True
    elif(num == ln):
        lcd.putstr('ln')
        ln_op = True
    elif(num == enter):
        calculate(str_op)
    #Number Update
    if(first):
        strnum1 += tempnum
    else:
        strnum2 += tempnum
    

def calculate(oper):
    placeholder = 10.0
    answer = 0.0
    lcd.move_to(0,1)
    if(oper == ''):
        try:
            answer = float(strnum1)
        except ValueError:
            answer = "Error"
    elif(oper == '+'):
        try:
            answer = float(strnum1) + float(strnum2)
        except ValueError:
            answer = "Error"
    elif(oper == '-'):
        try:
            answer = float(strnum1) - float(strnum2)
        except ValueError:
            answer = "Error"
    elif(oper == '*'):
        try:
            answer = float(strnum1) * float(strnum2)
        except ValueError:
            answer = "Error"
    elif(oper == '/'):
        try:
            answer = float(strnum1) / float(strnum2)
        except ZeroDivisionError:
            answer = "Error"
#Log/Ln check
    if(log_op):
        try:
            answer = math.log10(answer)
        except ValueError:
            answer = "Error"
    elif(ln_op):
        try:
            answer = math.log(answer)
        except ValueError:
            answer = "Error"
    
    lcd.putstr(str(answer))

#Initializations
lcd.clear()
lcd.move_to(0,0)

while True:
    if(p0.debounced_read_cooldown()):
        screenUpdate(p0)
    elif(p1.debounced_read_cooldown()):
        screenUpdate(p1)
    elif(p2.debounced_read_cooldown()):
        screenUpdate(p2)
    elif(p3.debounced_read_cooldown()):
        screenUpdate(p3)
    elif(p4.debounced_read_cooldown()):
        screenUpdate(p4)
    elif(p5.debounced_read_cooldown()):
        screenUpdate(p5)
    elif(p6.debounced_read_cooldown()):
        screenUpdate(p6)
    elif(p7.debounced_read_cooldown()):
        screenUpdate(p7)
    elif(p8.debounced_read_cooldown()):
        screenUpdate(p8)
    elif(p9.debounced_read_cooldown()):
        screenUpdate(p9)
    elif(dec.debounced_read_cooldown()):
        screenUpdate(dec)
    elif(cl.debounced_read_cooldown()):
        screenUpdate(cl)
    elif(enter.debounced_read_cooldown()):
        screenUpdate(enter)
    elif(add.debounced_read_cooldown()):
        screenUpdate(add)
    elif(subt.debounced_read_cooldown()):
        screenUpdate(subt)
    elif(mult.debounced_read_cooldown()):
        screenUpdate(mult)
    elif(div.debounced_read_cooldown()):
        screenUpdate(div)
    elif(log.debounced_read_cooldown()):
        screenUpdate(log)
    elif(ln.debounced_read_cooldown()):
        screenUpdate(ln)