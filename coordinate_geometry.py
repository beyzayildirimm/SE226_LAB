import math  # python karekökü bilmiyormuş
x1=float(input("Enter X1:"))
y1=float(input("Enter Y1:"))
x2=float(input("Enter X2:"))
y2=float(input("Enter Y2:"))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Distance: {distance} .")
