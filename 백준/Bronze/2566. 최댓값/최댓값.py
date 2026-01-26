
list_b = [0]*9
for i in range(9):
    list_a = list(map(int,input().split()))
    list_b[i] = list_a
max_result = -1

for j in range(9):
    if max_result < max(list_b[j]):
        max_result = max(list_b[j])
        first = j+1
        second = list_b[j].index(max_result)+1
print(max_result)
print(first, second)
