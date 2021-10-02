def solution(progresses, speeds):
    
    prior_task_day = 0
    cnt = 0
    result = []
    
    for p, s in zip(progresses, speeds):
        
        left_percent = 100 - p
        day_to_finish = left_percent // s + (left_percent % s != 0)
        
        if prior_task_day < day_to_finish:
            if cnt != 0:
                result.append(cnt)
                cnt = 0
            prior_task_day = day_to_finish
        cnt += 1
    result.append(cnt)
    return result