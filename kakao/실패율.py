def solution(N, stages):
    fail_per_stage = {}

    for i in range(1, N+1):
        gte = list(filter(lambda x:x>=i, stages))
        equal = gte.count(i)
        if gte:
            fail_per_stage[i] = equal / len(gte)
        else:
            fail_per_stage[i] = 0
        fail_per_stage = dict(sorted(fail_per_stage.items(), key=lambda x:x[1], reverse=True))
    
    return list(fail_per_stage.keys())
    
