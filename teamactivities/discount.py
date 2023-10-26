from datetime import datetime

#main variables

#discount rate is 10% and sales tax rate is 6%
discrate = 0.10
taxrate = 0.06


subtotal=float(input("please enter sub-total:"))
current_datetime = datetime.now()

weekday = current_datetime.weekday()

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * discrate, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount

sales_tax = round (subtotal *taxrate, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

total = subtotal + sales_tax

print(f"Total: {total:2f}")
print(f"Date: {current_datetime}")






































































