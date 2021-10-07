from collections import Counter
def solution(clothes):
    values = list(Counter([cloth[1] for cloth in clothes]).values())
    answer = 1
    for v in values:
    	answer *= (v+1)
    return answer -1


# Reduce를 이용한 풀이

from collections import Counter
from itertools import reduce
def solution(clothes):
    values = list(Counter([cloth[1] for cloth in clothes]).values())
    return reduce(lambda a, b: a*(b+1), values, 1) - 1
