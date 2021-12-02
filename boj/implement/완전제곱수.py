m = int(input())
n = int(input())

import math
total = 0
min_value = n+1
for num in range(m, n+1):
	# print(math.sqrt(num))
	if not math.sqrt(num) % 1:
		total += num
		min_value = min(min_value, num)

if not total:
	print(-1)
else:
	print(total)
	print(min_value)