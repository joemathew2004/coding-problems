"""
Find the minimum number of moves to reduce a number to 0.
In each move, you can either divide by 2 (if even) or subtract 1.
"""

def min_moves(n):
    moves = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        moves += 1
    return moves

if __name__ == "__main__":
    print(min_moves(6))   # Output: 3
    print(min_moves(10))  # Output: 4