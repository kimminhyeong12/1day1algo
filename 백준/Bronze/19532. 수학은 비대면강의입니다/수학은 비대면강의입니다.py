a,b,c,d,e,f = map(int,input().split())
for x in range(-999,1000):
    for y in range(-999,1000):
        if a*x+b*y ==c and d*x + e*y == f:
            x_result = x
            y_result = y
print(x_result,y_result)
