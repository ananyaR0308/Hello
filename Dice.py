import random as r
import time as t
print("Welcome guys!!! this is Dice game")
t.sleep(1)
print("1-Role the Dice")
t.sleep(1)
print("2-Exit")
t.sleep(1)
Option=int(input("Enter Option:- "))
t.sleep(1)
Dice_No=r.randint(1,6)
while True:
    if Option==1:
      if Dice_No==6:
         print("Woww!!")
      else:
         print(Dice_No)
      break
    if Option==2:
       print("Thank you!! For visit us..")
       break