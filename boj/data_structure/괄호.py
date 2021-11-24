n = int(input())

for _ in range(n):
    ps = input()
    if len(ps) % 2:
        print("NO")
        continue
    open_p = 0
    for p in ps:
        if p == "(":
            open_p += 1
        else:
            open_p -= 1
        if open_p < 0:
            break
    if open_p:
        print("NO")
    else:
        print("YES")
