paper = [[0] * 100 for _ in range(100)]
n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            paper[j][k] = 1
result = 0
for _ in paper:
    result += sum(_)
print(result)