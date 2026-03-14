import math

print("Quadratic Equation Solver")
print("Equation form: ax^2 + bx + c = 0")

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b*b - 4*a*c   # discriminant

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    
    print("Two real roots:")
    print(root1)
    print(root2)

elif d == 0:
    root = -b / (2*a)
    
    print("One real root:")
    print(root)

else:
    print("No real roots")