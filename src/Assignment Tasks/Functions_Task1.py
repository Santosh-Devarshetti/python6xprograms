# Q - Create a function which will take a positive number from the user and perform square of the number?
# i/o = 3
# o/p = 9

def exp(x):
    return x*x
i = int(input("enter a valid number:"))
result=exp(i)
print(f"square of given number:{i} is",result)

# Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

def triangletype(x,y,z):
    if x==y and y==z and x==z:
        print("Equlateral triangle")
    elif x==y or y==z or x==z:
        print("Isometric triangle")
    else:
        print("scalene triangle")

i,j,k = map(int,(input("enter three numbers:").split()))
triangletype(i,j,k)