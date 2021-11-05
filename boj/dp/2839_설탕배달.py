weight = int(input())
cnt = 0
while weight:

    if weight % 5 == 0:
        print(cnt + weight // 5)
        break
    weight -= 3
    cnt += 1
    if weight < 0:
        print(-1)
        break
    if weight == 0:
        print(cnt)
