# Question 3 :
# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
# Hint: Use a counter (like wait_time) and break condition.
pageload_time = [0,5,9]
i= 0
while i<len(pageload_time):
    time = pageload_time[i]
    if time <= 5:
        print(f"page load time {i+1} is Success")
        # break
    else:
        print(f"page load time {i+1} is Failed")
    i= i + 1




