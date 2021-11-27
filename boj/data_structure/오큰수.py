n = int(input())

seq = list(map(int, input().split()))

result = [-1] * len(seq)
stack = []
for i in range(n):
	while stack and seq[stack[-1]] < seq[i]:
		result[stack.pop()] = seq[i]
	stack.append(i)

print(*result)