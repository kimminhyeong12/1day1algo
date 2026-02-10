n = int(input())
def find_min(n):
    dp = [float('inf')]*(n+5)
    dp[3] = 1
    dp[5] = 1
    for i in range(6,n+1):
        dp[i] = min(dp[i-3],dp[i-5]) +1
    if dp[n] < float('inf'):
        return dp[n]
    else:
        return -1
print(find_min(n))