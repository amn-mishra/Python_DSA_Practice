import math


def minStepsTo1Help(n, dp):
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        val1 = 10000
        for j in range(1, int(math.sqrt(i)) + 1):
            this = 1 + dp[i - (j * j)]
            val1 = min(this, val1)
        dp[i] = val1
    return dp[n]


def minStepsTo1(n):
    dp = [-1 for i in range(1 + n)]
    ans = minStepsTo1Help(n, dp)
    return ans

ans = minStepsTo1(1000)
print(ans)





