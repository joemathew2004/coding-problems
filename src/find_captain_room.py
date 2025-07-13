"""
Find the captain's room number in a hotel where each family has k members
except the captain's family which has only 1 member.
"""

from collections import Counter

def find_captain_room_v1(k, room_list):
    """Version 1: Using Counter"""
    freq = Counter(room_list)
    for room, count in freq.items():
        if count != k:
            return room

def find_captain_room_v2(k, room_list):
    """Version 2: Using mathematical approach"""
    total = sum(room_list)
    unique_rooms = set(room_list)
    sum_unique = sum(unique_rooms)
    captain = (k * sum_unique - total) // (k - 1)
    return captain

if __name__ == "__main__":
    k = 5
    room_list = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
    
    print("Captain's room (v1):", find_captain_room_v1(k, room_list))
    print("Captain's room (v2):", find_captain_room_v2(k, room_list))