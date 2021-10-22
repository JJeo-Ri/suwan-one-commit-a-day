def solution(board, moves):
    board = list(map(list, zip(*board))) # 행렬 바꾸기
    board = [list(filter(lambda x: x>0, b)) for b in board] # 0보다 큰놈만 남기기

    box = [-1]
    score = 0
    for move in moves:
        move = move - 1
        if board[move]:
            item = board[move].pop(0)
            if item == box[-1]: # 현재 아이템과 마지막 아이템이 같으면
                score += 2 # 점수는 2점
                box.pop(-1) # 마지막 아이템 빼주기
            else:
                box.append(item)
        
    return score

