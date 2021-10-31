def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        learn = ''.join(list(filter(lambda x: x in skill, tree)))
        if learn == skill[:len(learn)]:
            answer += 1
    return answer
