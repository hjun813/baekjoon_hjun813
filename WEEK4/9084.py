import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())
    coinValue = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] =1
    print(dp)
    for coin in coinValue:
        print("coin", coin)
        for i in range(coin,M+1):
            print('i', i)
            dp[i] += dp[i - coin]
            print(dp)
            print()
    
    print(dp[-1])


