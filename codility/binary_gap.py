def solution(N):
    zero_cnt = 0
    result = []
    for k in bin(N)[2:]:
        if k == '1':
            result.append(zero_cnt)
            zero_cnt = 0
        else:
            zero_cnt += 1
    return max(result)
