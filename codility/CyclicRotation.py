def solution(A, K):
    for _ in range(K):
        A = A[-1:] + A[:-1]
    return A

from collections import deque
def solution(A, K):
    A = deque(A)
    A.rotate(K)
    return list(A)
