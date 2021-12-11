target = int(input())
number = 0
i = 1
while True:
	number += i
	if number == target:
		print(i)
		break
	elif number > target:
		print(i-1)
		break

	i += 1
