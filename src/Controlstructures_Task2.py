# Q2
# In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.
# expected_title = "Dashboard"
# actual_title = "Dashboard "
# ✅ Test Passed – Title matches
# True - why >  Strip and convert them into the lowercase = both of them are equal.
expected_title = "Dashboard"
actual_title = input("enter the actual title: ").strip()
# print(expected_title,actual_title)
if expected_title.lower() == actual_title.lower():
    print("✅ Test Passed – Title matches")
else:
    print("❌ Failed Title was not matched:")
