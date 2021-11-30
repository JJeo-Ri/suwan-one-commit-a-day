import heapq

n = int(input())
cards = []
for _ in range(n):
	heapq.heappush(cards, int(input()))
if n == 1:
	print(0)
else:
	result = 0
	while True:
		min_1 = heapq.heappop(cards)
		min_2 = heapq.heappop(cards)
		new_value = min_1+min_2
		result += new_value
		heapq.heappush(cards, new_value)

		if len(cards) == 1:
			break
	print(result)