n,m = map(int,(input().split()))
list_a = []
list_a += map(int,input().split())
max = -1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (list_a[i]+list_a[j]+list_a[k]) > max and (list_a[i]+list_a[j]+list_a[k]) <= m:
                max = list_a[i]+list_a[j]+list_a[k]
print(max)
