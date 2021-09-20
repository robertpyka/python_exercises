#Program read number of days,hours,minutes and seconds. Then show number of seconds for sum of them

days = int(input("Number of days:"))
hours = int(input("Number of hours:"))
minutes = int(input("Number of minutes:"))
seconds = int(input("Number of seconds:"))
total_seconds = seconds + minutes * 60 + hours * 3600 + days * 3600 * 24

print(f'Total number of seconds is {total_seconds}')