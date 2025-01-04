import sys
sys.setrecursionlimit(10000000)

def solution(k, room_number):
    answer = []
    parent = {}

    def find(room):
        if room not in parent:
            parent[room] = room + 1 
            return room
        parent[room] = find(parent[room])
        return parent[room]

    for room in room_number:
        assigned_room = find(room)
        answer.append(assigned_room)

    return answer