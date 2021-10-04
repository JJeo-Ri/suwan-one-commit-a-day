# 나의 풀이 (시간초과)

def solution(numbers, target):

    cnt = 0
    for i in range(2 ** len(numbers)):
        seq = bin(i)[2:].zfill(len(numbers))

        k = (eval(''.join([["-", "+"][int(b)] + str(n) for n, b in zip(numbers, seq)])))
        if k == target:
            cnt += 1

    return cnt


# 정답 풀이

def solution(numbers, target):
    sup= [0]
    for i in numbers:
        sub = []
        for j in sup :
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
    return sup.count(target)
