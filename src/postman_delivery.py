"""
A postman needs to deliver mail to houses on a street. 
Find the minimum distance to deliver all mail starting from position 0.
"""

def solve():
    N, C = map(int, input().split())
    
    positive_locations = []
    negative_locations = []
    
    for _ in range(N):
        coord, mail_amount = map(int, input().split())
        if coord > 0:
            positive_locations.append((coord, mail_amount))
        else:
            negative_locations.append((coord, mail_amount))
            
    positive_locations.sort(key=lambda x: x[0], reverse=True)
    negative_locations.sort(key=lambda x: x[0])
    
    total_distance = 0
    
    # Handle positive locations
    current_capacity = 0
    for coord, mail_amount in positive_locations:
        while mail_amount > 0:
            if current_capacity == 0:
                total_distance += 2 * coord
                current_capacity = C
            
            take = min(mail_amount, current_capacity)
            mail_amount -= take
            current_capacity -= take

    # Handle negative locations
    current_capacity = 0
    for coord, mail_amount in negative_locations:
        while mail_amount > 0:
            if current_capacity == 0:
                total_distance += 2 * abs(coord)
                current_capacity = C
            
            take = min(mail_amount, current_capacity)
            mail_amount -= take
            current_capacity -= take
            
    print(total_distance)

if __name__ == "__main__":
    solve()