"""
Count the number of negative numbers in a sorted matrix 
(rows and columns in non-increasing order).
"""

def count_negatives(grid, n, m):
    count = 0
    row, col = n - 1, 0  # Start from the bottom-left corner

    while row >= 0 and col < m:
        if grid[row][col] < 0:
            count += (m - col)  # Add all negative numbers in this row
            row -= 1  # Move up
        else:
            col += 1  # Move right

    return count

if __name__ == "__main__":
    n = int(input())  
    m = int(input())  
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(count_negatives(grid, n, m))