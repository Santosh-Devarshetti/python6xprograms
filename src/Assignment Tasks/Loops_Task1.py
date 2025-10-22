# Given a Number a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1,

number = int(input("enter number: "))
fact = 1
for i in range(number,1,-1):
    fact= fact*i
print(fact)
