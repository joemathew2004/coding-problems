"""
Find the longest subarray where prices are strictly increasing.
"""

def longest_increasing_subarray(prices):
    if not prices:
        return []

    max_len = 1
    start = 0
    max_start = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            if i - start + 1 > max_len:
                max_len = i - start + 1
                max_start = start
        else:
            start = i 

    return prices[max_start:max_start + max_len]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = longest_increasing_subarray(arr)
    print(' '.join(map(str, result)))