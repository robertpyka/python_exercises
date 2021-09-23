# Program takes integers from users, and sort them.
# If user input equal 0, program will print all values sorted


list = []
x = int(input("Give value: "))
while x!=0:
    list.append(x)
    x = int(input("Give value: "))


list.sort()
for item in list:
    print(item)
