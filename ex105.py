# Program get values from user, and print them in reversed order.
# 0 stop reading values

list = []
x = int(input("Give value:"))
while x != 0:
    list.append(x)
    x = int(input("Give value:"))

list.reverse()

for item in list:
    print(item)
