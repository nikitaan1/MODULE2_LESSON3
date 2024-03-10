#Task 1

try:
    x = 1 / 0
except ZeroDivisionError:
    pass

#Task 2


try:
    x = "12" + 3
except TypeError:
    pass

          
#Task 3

filename = input("Please enter the filename to read: ")

if filename == "readme.md":
        print("Open File")
else:
        pass
