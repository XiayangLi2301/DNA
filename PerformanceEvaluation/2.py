dp = [0 for i in range(100)]
def find(n):
    if n == 1 :
        dp[0] = 1
    if n == 2:
        dp[0] = 1
        dp[1] = 2
    if n > 2:
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
    return dp[n-1]
if 'name'=='main':
    print(find(100))

