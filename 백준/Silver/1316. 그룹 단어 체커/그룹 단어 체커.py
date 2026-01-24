def checker(list_a):
    count = 0
    for i in range(len(list_a)):
        a = [0] * 26
        group = True
        for j in range(len(list_a[i])):
            index = ord(list_a[i][j]) - 97
            if a[index] ==0:
                a[index] = True
            elif a[index] == True:
                if list_a[i][j] == list_a[i][j-1]:
                    continue
                else:
                    group = False
        if group:
           count +=1


    return count



n = int(input())
list_a = [0]*n
for i in range(n):
    list_a[i] = input()
print(checker(list_a))
