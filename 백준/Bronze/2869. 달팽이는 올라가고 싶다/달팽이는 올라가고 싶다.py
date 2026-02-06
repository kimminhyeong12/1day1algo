import math
a,b,v = map(int,input().split())
day_meter = a-b
day = math.ceil((v - a) / day_meter) +1
print(day)



