n = list(input())

n.sort(reverse=True)
num = ''.join(n)

if int(num) % 30 == 0:
	print(int(num))
else:
	print(-1)