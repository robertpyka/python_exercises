# Program look for all perfect numbers, what mean sum of all proper divisor is qeual to number which is checked
sum_proper = 0
perfect_numbers = []
for i in range(1,10000):
    for j in range(1 , i):
        if i % j == 0:
            sum_proper = sum_proper+j
    if sum_proper == i:
        perfect_numbers.append(i)
    sum_proper = 0
print(perfect_numbers)

