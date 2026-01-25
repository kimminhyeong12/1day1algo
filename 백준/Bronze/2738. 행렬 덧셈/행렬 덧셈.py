n,m = map(int,input().split())

list_a = []
list_b = []
for i in range(n):
    list_a.append(list(map(int,input().split())))
for j in range(n):
    list_b.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        print(list_a[i][j]+list_b[i][j], end = " ")
    print()
