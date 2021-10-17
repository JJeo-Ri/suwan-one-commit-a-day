def solution(citations):
    citations.sort(reverse=True)
    
    for i, c in enumerate(citations):
        if i >= c:
            return i
    return len(citations) # i가 c이상이 될 수 없는 경우는 모든 논문의 인용수가 논문의 수보다 많을 때이다.

# 우주인의 풀이

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
