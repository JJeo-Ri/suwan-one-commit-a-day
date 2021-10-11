# 마치 컨테이터 벨트
def solution(bridge_length, weight, truck_weights):
    time = 0
    
    on = [0] * bridge_length
    
    while len(on) != 0:
        time += 1
        
        on.pop(0)
        
        if truck_weights:
            if sum(on) + truck_weights[0] <= weight:
                on.append(truck_weights.pop(0))
            else:
                on.append(0)
    return time
        

# import uuid
# def solution(bridge_length, weight, truck_weights):
#     in_bridge_weight = 0
#     passed = []
#     in_bridge = []
#     yet = truck_weights
#     time = 0
#     my_dict = dict()
#     while yet or in_bridge:
#         time += 1

#         for i, v in my_dict.items():
#             if time - v == bridge_length:
#                 passed.append(in_bridge.pop(0))
#         if yet:
#             if sum(in_bridge) + yet[0] <=  weight:
#                 in_bridge.append(yet.pop(0))
#                 my_dict[uuid.uuid1()] = time
#     return time
