# Q3
# You want to check whether a web page loads within 3 seconds (performance test condition).
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds
loadtime = float(input("Enter the page load time in seconds: "))
if loadtime > 3.0:
    print(f"⚠️ Page load too slow: {loadtime} seconds")
else:
    print(f"✅ Page loaded within acceptable time: {loadtime} seconds")
