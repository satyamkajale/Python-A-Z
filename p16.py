# wapp to read radius of circle from user and print and circumference of circle

radius = float(input("enter radius of circle "))

area = 3.14159 * radius ** 2
circumference = 2 * 3.14159 * radius

print("area = ", round(area,2))
print("circumference = ", round(circumference,2))
