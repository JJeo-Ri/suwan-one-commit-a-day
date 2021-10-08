def solution(prices):
    # 시간초과..
    # result = []
    # for i, target in enumerate(prices):
    #     for j, other in enumerate(prices[i+1:]):
    #         if target > other:
    #             result.append(j+1)
    #             break
    #     else:
    #         result.append(len(prices[i+1: ]))
    # return result

    # 이중 for 사용하면 안된다.!!
    # for target in prices:
    #     for target in prices:
    #         pass

    # 시간초과
    # result = []
    # for i, p in enumerate(prices):
    #     _under = list(map(lambda x: (x<p), prices[i+1:]))
    #     if sum(_under) == 0:
    #         result.append(len(prices[i+1:]))
    #     else:
    #         result.append(_under.index(True)+1)
    # return result

    # 성공
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    return answer

# PRICE 길이 DEBUGGING
#     if len(prices) < 50000:
#         return Error

#     for target in prices:
#         for target in prices:
#             pass

    # 시간 초과
#     for i in range(len(prices)):
#         for j in range(len(prices)):
#             pass
