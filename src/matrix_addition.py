"""
Read two matrices of the same dimensions and compute their element-wise sum.
"""

def matrix_addition():
    r, c = input().split()      
    rows = int(r)
    cols = int(c)

    matrix1 = []              
    matrix2 = []  

    for i in range(rows):
        matrix1.append(input().split())

    for j in range(rows):
        matrix2.append(input().split())

    print('First Matrix:')
    for row in matrix1:
        print(' '.join(row))

    print('Second Matrix:')
    for row in matrix2:
        print(' '.join(row))

    print('Sum of the two matrices is:')
    for i in range(rows):
        for j in range(cols):
            sum_val = int(matrix1[i][j]) + int(matrix2[i][j])
            print(sum_val, end=' ')
        print()

if __name__ == "__main__":
    matrix_addition()