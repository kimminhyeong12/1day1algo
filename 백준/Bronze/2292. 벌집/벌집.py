def bee_house(n):
    count = 1
    result = 1
    a = 6
    while(result < n):
        result += a
        a += 6
        count +=1
    return count

n = int(input())
print(bee_house(n))