cnt = 1
while True:
	l, p, v = map(int, input().split())
	if l + p + v == 0:
		break
	vacation = l * (v // p) + min(v % p, l)
	print(f"Case {cnt}: {vacation}")
	cnt += 1
