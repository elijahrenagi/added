import math

num_items = int(input("Enter the number of Manufactured Items"))
num_boxes = int(input("Enter the number of items the user will pack per box"))

boxes = math.ceil(num_items/ num_boxes)

print (f"You will need {boxes} boxes to pack {num_boxes} items in each box")