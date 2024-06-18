def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    second =0
    current_weight = 0
    while truck_weights :
        second +=1

        if bridge[0]!=0 :
            current_weight -= bridge[0]
        bridge.pop(0)
        bridge.append(0)
        incomming = truck_weights[0]

        if current_weight + incomming <= weight :
            bridge [-1] = truck_weights.pop(0)
            current_weight +=incomming

    return second + bridge_length