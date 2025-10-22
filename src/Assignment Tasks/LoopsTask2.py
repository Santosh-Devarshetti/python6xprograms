# Question 2 :
# An API sometimes fails due to network delays.
# Write a program to retry the API call 3 times until the response code becomes 200.
# If it still fails after 3 tries, print a failure message.
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# ✅ Test Passed
# i=1
# while i <= 10:
#     print(i)
#     i = i + 1
responsecode = [300,400,200]
i = 0
while i<len(responsecode):
    code = responsecode[i]
    if code == 200:
        print(f"Attempt {i}: Response code\n ✅ Test Passed ")
    else:
        print(f"Attempt {i}: Response code\n ❌Test failed ")
    i = i + 1

