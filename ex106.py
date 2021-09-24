# Program will remove 2 largest and lowest values, from list.
# If user give less than 5 numbers, program will show proper message. 00 stop the program
# function which removes highest and lowest values from list
def remove_values(list_of_numbers, num):
    for i in range(num):
        list_of_numbers.pop(-1)
        list_of_numbers.pop(0)


list_of_values = []

x = int(input("Give value:"))
while x != "0":
    list_of_values.append(x)
    x = int(input("Give value:"))

# declare how many highest and lowest values should be removed
to_remove = 2
list_of_values.sort()

if len(list_of_values) <= 2 * to_remove:
    print("Wrong amount of values")
else:
    remove_values(list_of_values, to_remove)
    print(list_of_values)
