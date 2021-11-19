n = int(input())
seq = [int(input()) for _ in range(n)]
if n == 1 or n == 2:
    print(sum(seq))
else:
    dp = []

    dp.append(seq[0])
    dp.append(seq[0] + seq[1])
    dp.append(max(seq[0] + seq[2], seq[1]+seq[2]))

    for i in range(3, len(seq)):
        dp.append(max(dp[i-2]+seq[i], dp[i-3]+seq[i-1]+seq[i]))

    print(dp[-1])