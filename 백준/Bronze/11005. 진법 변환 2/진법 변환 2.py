import sys

N, B = map(int, sys.stdin.readline().split())
table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while N > 0:
    N, remainder = divmod(N, B)
    result += table[remainder]

print(result[::-1])