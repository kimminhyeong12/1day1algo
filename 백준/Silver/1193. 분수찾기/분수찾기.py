n = int(input())
count = 0
k = 1
result = 0
while (count<n):
    count = count + k
    k = k+1
    result +=1
parent = result
child = 1
while(count!=n):
    parent -= 1
    child +=1
    count -=1
if (result%2==0):
    result = str(parent) + "/" + str(child)
else:
    result = str(child)+"/"+str(parent)
print(result)

