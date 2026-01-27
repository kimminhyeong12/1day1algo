list_a = [list(input()) for _ in range(5)]
for i in range(15):
    for j in range(5):
        if i < len(list_a[j]):
            print(list_a[j][i], end ="")

