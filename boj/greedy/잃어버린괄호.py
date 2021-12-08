exp = input()
# 55-50+40
for i, sub in enumerate(exp.split("-")):
	sub = '+'.join([str(int(num)) for num in sub.split("+")])
	value = eval(sub)
	if i == 0:
		result = value
	else:
		result -= value

print(result)