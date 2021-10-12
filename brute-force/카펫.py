def solution(b, y):
    num = b + y
    # x가 더 크거나 같다.
    for x in range(num // 2 + 1, 2, -1):
        if num % x != 0:
            continue
        y = num // x
        if 2*x + 2*y == b+4:
            return [x, y]
