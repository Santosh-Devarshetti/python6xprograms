print("hello world")
print("hello world of python", "congrats", " for your first program",sep = "|")
print("apple","banana","cherry", sep="|")
print("A","B","C","E",sep="-")
print("Python","rocks",sep ="-",end="|Always\n")
print("hello world from Python",end="!\n")
print("one ",end = "")
print("two ",end = "")
print("three ",end = "")
print("A","B","C","D","E","F",sep = "*",end ="$\n")
print("F","G","H","I","J","K",sep = "*",end ="$\n")
#Red, Green, Blue...Done!
print("Red","Green","Blue...",sep=",",end="Done!\n")
# Python | 3.12 | Awesome
print("Python "," 3.12 "," Awesome ",sep="|")

print(type(1.1))
print(type(True))
print(type("abc"))
print("enter type of testing u want to perform")
type = input("please enter Automation.DB.Security,Manual,performance,API: ").strip()
type = type.lower()
match type:
    case "autmation":
        print("You have choosen Aumations testing:")
    case "db":
        print("You have choosen DB testing:")
    case "security":
        print("You have choosen Security testing:")
    case "api":
        print("You have choosen API testing:")
    case "manual":
        print("You have choosen Manual testing:")
    case "performance":
        print("You have choosen Performance testing:")

    case _:
        print("enter valid type")

day = input("please enter day: ").strip()
match day:
    case "1":
         print("today is monday")
    case "2":
        print("today is tuesday")
    case "3":
        print("today is wednesday")
    case "4":
        print("today is thursday")
    case "5":
        print("today is friday")
    case "6":
        print("today is saturday")
    case "7":
        print("today is sunday")
    case _:
        print("enter valid day")
