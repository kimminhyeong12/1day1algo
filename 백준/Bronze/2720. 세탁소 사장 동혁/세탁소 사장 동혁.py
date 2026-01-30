list_a = []
n = int(input())
for i in range(n):
    change = int(input())
    a, b, c, d = 0, 0, 0, 0
    while change > 0:
        if change // 25 >= 1:
            a = change // 25
            change = change - (25*a)
        elif change // 10 >= 1:
            b = change // 10
            change = change - (10*b)
        elif change // 5 >= 1:
            c = change // 5
            change = change - (5*c)
        elif change // 1 >= 1:
            d = change // 1
            change = change - (1*d)
    list_a.append([a,b,c,d])
for i in range(len(list_a)):
    for j in range(len(list_a[i])):
        print(list_a[i][j], end = " ")
    print()

