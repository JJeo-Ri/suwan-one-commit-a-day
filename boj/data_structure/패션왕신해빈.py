from collections import defaultdict

n = int(input())

for _ in range(n):
	m = int(input())
	clothes = defaultdict(int)
	for _ in range(m):
		name, category = input().split()
		clothes[category] += 1
	days = 1
	for cnt in clothes.values():
		days *= cnt + 1
	print(days-1)
