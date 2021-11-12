from itertools import zip_longest

def solution(A):
    A.sort()
    B = range(1, len(A) + 2)
    for a, b in zip_longest(A, B):
        if a != b:
            return b


def solution(A):
    return sum(range(len(A)+2)) - sum(A)
 
