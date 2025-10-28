#Test 1: Print even numbers between 1 and 20
for i in range(1,21,1):
    if i % 2 == 0:
        print(i)
print("----------------------")
#Task 2: Print numbers from 10 down to 1
for i in range(10,0,-1):
    print(i)
#Test 3: Skip numbers divisible by 3, from (0,100)
print("----------------------")
for i in range(1,101,1):
    if i%3==0:
        continue
    else:
        print(i)
