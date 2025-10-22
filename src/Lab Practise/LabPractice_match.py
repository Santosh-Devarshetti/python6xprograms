a,b = map(int,(input("enter two values").split(",")))
print(a,b)
operator = input("enter operator +,-,*,/,%: ")
print(operator)
match operator:
    case "+":
        print("addition:",(a+b))
    case "*":
        print("Multiplication:",(a*b))
    case "-":
        print("Substraction:",(a-b))
    case "/":
        print("Division:",(a/b))
    case "%":
         print("Modulus:",(a%b))
    case _:
        print("invalid operator")

stuper= int(input("enter student percentage: ").strip())
print(stuper)
match stuper:
    case s if s > 45 and s < 60:
        print("first class:",s)
    case s if s > 61 and s < 70:
        print("Distinction:",s)
    case s if s > 71 and s < 100:
        print("Top class:",s)
    case _:
        print("Invalid class:",s)