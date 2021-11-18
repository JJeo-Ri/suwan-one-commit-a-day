n = int(input())

seq = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
	seq[i][0] += min(seq[i-1][1], seq[i-1][2])
	seq[i][1] += min(seq[i-1][0], seq[i-1][2])
	seq[i][2] += min(seq[i-1][0], seq[i-1][1])
	
print(min(seq[-1]))
