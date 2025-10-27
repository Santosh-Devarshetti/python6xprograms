lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
name = ["santosh","Valtech",2023,1407,"Bengaluru"]
#printing the list items
for i in range(0,(len(name)-1)):
    print(name[i])
#modifying the list items
print("---------------------")
name[1]="Valtech India System"
for item in name:
    print(item)
print("---------------------")
name.append("JP Nagar")
for item in name:
    print(item)