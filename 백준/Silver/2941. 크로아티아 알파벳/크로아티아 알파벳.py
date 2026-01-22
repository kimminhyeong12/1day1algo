def cro(n):
    count = 0
    for i in range(len(n)):
        count +=1
        if n[i] == "=":
            if i>1 and n[i-1] == "z" and n[i-2] == "d":
                count -= 1
            if i >0 and n[i-1] in "csz":
                count -= 1

        elif n[i] == "-":
            if n[i-1] in "cd":
                count -= 1
        elif n[i] == "j":
            if n[i-1] in "ln":
                count -=1
            else:
                continue
    return count

n = input()
print(cro(n))
