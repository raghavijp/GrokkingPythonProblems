import math


def calculate_distance_to_0(matrix):
    m, n = len(matrix), len(matrix[0])

    for r in range(m):
        for c in range(n):

            if matrix[r][c] > 0:

                above = matrix[r-1][c] if r > 0 else  math.inf
                left = matrix[r][c-1] if c > 0 else math.inf

                matrix[r][c] = min(above, left) + 1

    for r in range(m-1, -1, -1):
        for c in range(n-1, -1, -1):

            if matrix[r][c] > 0:

                below = matrix[r+1][c] if r < m-1 else math.inf
                right = matrix[r][c+1] if c < n-1 else math.inf
                min_distance = min(below, right) + 1
                matrix[r][c] = min(matrix[r][c], min_distance)

    return matrix

def print_matrix(mat, name):
    print(f"{name}: ", end="\n")
    for i in range (len(mat)):
            print(mat[i],sep="\n")
    print("*"* 10)


def main():
    input_bits = [
        [[0, 1], [1, 1]],
        [[0, 0, 1], [0, 1, 1], [1, 0, 1]],
        [[0, 0, 0], [0, 1, 0], [1, 0, 1]],
        [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
        [[0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]],
    ]

    for i in range (len(input_bits)):
        print_matrix(input_bits[i], "given_array")
        calculate_distance_to_0(input_bits[i])
        print_matrix(input_bits[i], "distance_array")
        print("-" * 100)


if __name__ == "__main__":
    main()