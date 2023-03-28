# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [0 for i in range(bridge_length)]
    
#     while bridge:
#         answer += 1
#         bridge.pop(0)
#         if truck_weights:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 bridge.append(truck_weights.pop(0))
#             else:
#                 bridge.append(0)
    
#     return answer


def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = []
    time = []
    sum_bridge = 0
    while truck_weights or bridge:
        if time and time[0] == bridge_length:
            now = bridge.pop(0)
            time.pop(0)
            sum_bridge -= now

        if len(bridge) + 1 <= bridge_length and truck_weights:
            if truck_weights[0] + sum_bridge <= weight:
                now = truck_weights.pop(0)
                sum_bridge += now
                bridge.append(now)
                time.append(0)
        answer += 1
        time = list(map(lambda x: x + 1, time))
        
    return answer