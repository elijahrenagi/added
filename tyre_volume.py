#Author: Brother Elijah

#Importing Math Functions
import math
#Importing current date and time from system
from datetime import datetime

#Asking for the tyre values
w = float(input("enter the width of the tire in mm:"))
print()
r = float(input("enter the aspect ratio of the tire:"))
print()
d = float(input("enter the diameter of the wheel in inches"))
print()

num1 = 2540
brackets = (w*r)
num = 10000000000

#Computing volume
v = math.pi*w*w*r*(w*r+num1*d)/num

#This is the approximate volume
print(f"The approximate volume is {v:.2f} liters.")

#Exceeding Requirements
quest = input("Do you want to purchase this?")
print()
if quest == "yes".lower():
    ans = input("Please enter your contact number:")
if quest == "no".lower():
    ans = input("Please enter your contact number, we will get in touch!:")




current_date_and_time = datetime.now()
print(current_date_and_time)
#Printing to volume.txt
with open("volume.txt", "at") as volume_files:
    print(f"{current_date_and_time:%y-%m-%d},{w},{r},{d},{v:.2f},Contact Number:{ans},", file=volume_files)
