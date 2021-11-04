def solution(answers):
    sol1 = [1,2,3,4,5]
    sol2 = [2,1,2,3,2,4,2,5]
    sol3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [sum([answer == sol[i%len(sol)] for i, answer in enumerate(answers)]) for sol in [sol1, sol2, sol3]]
    
    return [i+1 for i, score in enumerate(scores) if max(scores) == score]
            
