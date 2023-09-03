# Python Program to read length and breadth of rect 
# find and print area and perimeter

length = float(input("enter length "))
breadth = float(input("enter breadth "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("area = ", area)
print("perimeter = ", perimeter)

print("area = ", round(area,2))
print("perimeter = ", round(perimeter,2))

