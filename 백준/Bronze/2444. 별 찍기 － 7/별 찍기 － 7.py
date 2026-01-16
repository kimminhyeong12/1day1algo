def print_star(n):
    star = 1
    gap = n-1
    while (star != 2*n-1 and gap !=0):
        print(" "*gap, end = "")
        print("*"*star)
        star +=2
        gap -=1
    while (star !=-1 and gap != 2*n-1):
        print(" " * gap, end="")
        print("*" * star)
        star -=2
        gap +=1

n = int(input())
print_star(n)