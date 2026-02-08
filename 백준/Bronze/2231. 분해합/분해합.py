n = int(input())
result = 0
for i in range(1,n+1):
    candidate = i + sum(int(j) for j in str(i))
    if (candidate == n):
        result = i
        break
print(result)