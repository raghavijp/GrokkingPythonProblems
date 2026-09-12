def generate(numRows):
    triangle = []

    for row_num in range(numRows):
        row = [None for _ in range(row_num + 1)]

        row[0], row[-1] = 1, 1
        for i in range(1, len(row) -1 ):
            row[i] = triangle[row_num-1][i-1] + triangle[row_num-1][i]

        triangle.append(row)

    return triangle


def main():
    test_cases = [
        {"numRows": 1},
        {"numRows": 2},
        {"numRows": 3},
        {"numRows": 4},
        {"numRows": 5},
        {"numRows": 6}
    ]
    for i, case in enumerate(test_cases):
        print(f"\t {i+1}. given rows: ", case);
        print(f"\t triangle generated ", generate(case["numRows"]))
        print("-" * 100)

if __name__ == "__main__":
    main()