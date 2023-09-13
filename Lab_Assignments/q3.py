import math

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
angle_degrees = float(input("Enter the included angle in degrees: "))

angle_radians = math.radians(angle_degrees)

area = (1/2) * side1 * side2 * math.sin(angle_radians)

rounded_area = round(area, 2)

print(f"The area of the triangle is {rounded_area} square units.")

