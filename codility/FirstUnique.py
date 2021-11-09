from collections import Counter
def solution(A):
    for key, value in Counter(A).items():
        if value == 1:
            return key
    return -1
