import math

w = float(input("enter the width of the tire in mm:"))
r = float(input("enter the aspect ratio of the tire:"))
d = float(input("enter the diameter of the wheel in inches"))

num1 = 2540
brackets = (w*r)
num = 10000000000
v = math.pi*w*w*r*(w*r+num1*d)/num

print(f"The approximate volume is {v:.2f} liters.")

from datetime import datetime
current_date_and_time = datetime.now()
print