N, K = map(int, input().split())
coin = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
count = 0
for i in range(len(coin)):

    if coin[i] > K:
        if coin[i-1] <= K:
            K = K - (coin[i-1])
            print(K)
            count += 1
print(count)
