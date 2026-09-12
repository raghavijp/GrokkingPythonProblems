def checkSquare(match_sticks_arr):

    if not match_sticks_arr:
        return False

    L = len(match_sticks_arr)

    perimeter = sum(match_sticks_arr)

    possible_side = perimeter // 4

    if possible_side * 4 != perimeter:
        return False

    match_sticks_arr.sort(reverse=True)

    sums = [0 for _ in range(4)]

    def dfs(index):

        if index == L:
            return sums[0] == sums[1] == sums[2] == possible_side

        for i in range(4):

            if sums[i] + match_sticks_arr[index] <= possible_side:
                sums[i] += match_sticks_arr[index]

                if dfs(index + 1):
                    return True

                sums[i] -= match_sticks_arr[index]

        return False

    return dfs(0)


def main():
    match_sticks_arr = [3,3,3,3,4]
    print(f"\t Given arr: [ ", end="")
    for i in range(len(match_sticks_arr)):
        print(f"{match_sticks_arr[i]},",  end="")
    print(f"]", end="")
    print("\n\t Result:", checkSquare(match_sticks_arr))



if __name__ == "__main__":
    main()