from collections import Counter
def solution(A):
    return [key for key, value in Counter(A).items() if value % 2 == 1][0]
