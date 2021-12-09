seq = input()

compress = []
prev = seq[0]
for s in seq[1:]:
	if prev != s:
		compress.append(prev)
	prev = s
compress.append(prev)

print(min(compress.count('1'), compress.count('0')))
# print(compress)
