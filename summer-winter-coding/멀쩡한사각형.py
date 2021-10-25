# 첫번째 풀이 12/18

def solution(w, h):
    points = set()
    a = h/w
    for x in range(1, w+1):
        y = h*x/w
        # y = a*x
        if y <= h:
            points.add((x, y))
    for y in range(1, h+1):
        x = w*y/h
        # x = y/a
        if x <= w:
            points.add((x, y))
    return w*h - len(points)

# 두번째 풀이 14/18

import math
def solution(fw, fh):
    gcd = math.gcd(fw, fh)
    w = fw // gcd
    h = fh // gcd
    points = set()
    for x in range(1, w+1):
        y = h*x/w
        if y <= h:
            points.add((x, y))
    for y in range(1, h+1):
        x = w*y/h
        if x <= w:
            points.add((x, y))
    return fw*fh - len(points) * gcd

# 세번째 풀이 16/18

import math
def solution(fw, fh):
    if fw == 1 or fh == 1:
        return 0
    elif fw == fh:
        return fw * fh - fw
    gcd = math.gcd(fw, fh)
    w = fw // gcd
    h = fh // gcd
    points = set()
    a = h/w
    for x in range(1, w+1):
        y = h*x/w
        # y = a*x
        if y <= h:
            points.add((x, y))
    for y in range(1, h+1):
        x = w*y/h
        # x = y/a
        if x <= w:
            points.add((x, y))
    return fw*fh - len(points) * gcd


# 어느 천재의 풀이

import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))
