"""
Given two arrays of equal length, rearrange them to minimize 
the sum of products of corresponding elements.
"""

def minimize_sum_products():
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))

    v1.sort()
    v2.sort(reverse=True)

    total_sum = 0
    for i in range(n):
        total_sum += v1[i] * v2[i]
    
    print(total_sum)

if __name__ == "__main__":
    minimize_sum_products()