#Calculate area of triangle, having all lenghts
import math

s1 = int(input("Lenght of side 1 : "))
s2 = int(input("Lenght of side 2 : "))
s3 = int(input("Lenght of side 3 : "))
sum = (s1 + s2 + s3)/2
area = math.sqrt(sum * (sum-s1) * (sum-s2) * (sum-s3))
print(f'Area of triangle is {area}')