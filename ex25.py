#Program from given amount of seconds, show how much it is days, hours, minutes, seconds.

total = int(input("Amount of seconds: "))

days = int( total / (3600*24))
hours = int((total - days * (3600*24)) / 3600)
minutes = int((total - days * (3600*24) - hours * 3600) / 60)
seconds = total - days * (3600*24) - hours * 3600 - minutes*60
print(f'Days:{days}')
print(f'Hours:{hours}')
print(f'Minutes:{minutes}')
print(f'Seconds:{seconds}')