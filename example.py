import math

F1 = input("enter magnitude of 1st force :\n")
angle1 = int(input("enter angle of the first force in degrees:\n"))

F2 = input("enter magnitude of 2nd force :\n")
angle2 = input("enter angle of the 2nd force in degrees:\n")

F3 = input("enter magnitude of 3rd force :\n")
angle3 = input("enter angle of the 3rd force in degrees:\n")

F4 = input("enter magnitude of 4th force:\n")
angle4 = input("enter angle of 4th force in degrees:\n")

# convert the angles in radian
angle1 = 0.0
angle1 = math.radians(angle1)
angle2 = 0.0
angle2 = math.radians(angle2)
angle = 0.0
angle3 = math.radians(angle3)
angle = 0.0
angle4 = math.radians(angle4)

f1x = F1 * math.cos(angle1)
f1y = F1 * math.sin(angle1)

F2x = F2 * math.cos(angle2)
F2y = F2 * math.sin(angle2)

F3x = F3 * math.cos(angle3)
F3y = F3 * math.sin(angle3)

F4x = F4 * math.cos(angle4)
F4y = F4 * math.sin(angle4)

Fx = print(F1x + F2x + F3x + F4x)
Fy = print(F1y + F2y + F3y + F4y)

resultant_magnitude = math.sqrt(Fx * 2 + Fy * 2)
resultant_angle = math.tan2(Fy, Fx)

print("resultant magnitude is", resultant_magnitude)
print("angle of resultant is", resultant_angle)