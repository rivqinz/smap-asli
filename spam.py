import pyautogui as spam
import time



limit = input("Enter no. of message")
msg1 = ("Kamu dimana?")
msg2 = ("Mabar ga si")
msg3 = ("Tes program uas hehehe")

i = 0

time.sleep(5)

while i<int(limit):

    spam.typewrite(msg1)
    spam.press('Enter') 
    time.sleep(1)
    spam.typewrite(msg2)
    spam.press('Enter')
    time.sleep(1)
    spam.typewrite(msg3)
    spam.press('Enter')

    time.sleep(1)


i+=1