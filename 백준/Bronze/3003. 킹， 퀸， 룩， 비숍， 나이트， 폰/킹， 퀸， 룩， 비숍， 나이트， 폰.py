def check_pin(n):
    pin = [1,1,2,2,2,8]
    result = [0]*len(pin)
    for i in range(len(pin)):
        result[i] = pin[i]-n[i]
    for j in range(len(pin)):
        print(result[j], end = " ")



n = list(map(int,input().split()))
check_pin(n)
