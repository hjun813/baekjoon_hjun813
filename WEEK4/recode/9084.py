import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    N = int(input())
    coinValue = list(map(int, input().split()))
    M = int(input())

    dp = [0 for _ in range(M+1)]
    dp[0] = 1

    for coin in coinValue:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin] 
            # dp[i]가 i원을 내는 현재 까지 방법의 수 인데 새 금액인 coin을 쓸 수 있으면
            # i-coin에 coin 만큼의 돈을 내면 i 원이 되므로 
            # dp[i-coin] 의 경우의 수 만큼 dp[i] 도 늘어나게 된다.
            
    print(dp[-1])