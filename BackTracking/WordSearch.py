def depth_first_search(row, col, word, index, grid):
    if len(word) == index:
        return True

    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col]!= word[index]:
        return  False

    temp = grid[row][col]

    grid[row][col] = '*'

    for rowOffset, colOffset in [(0,1),[1,0],[0,-1],[-1,0]]:
        if depth_first_search(row+rowOffset, col+colOffset, word, index+1, grid):
            return True

    grid[row][col] = temp
    return False


def word_search(grid, word):
    n = len(grid)
    m = len(grid[0])

    for row in range(n):
        for col in range(m):
            if depth_first_search(row,col,word,0,grid):
                return True
    return False


def main():
    input = [
        ([['E', 'D', 'X', 'I', 'W'],
          ['P', 'U', 'F', 'M', 'Q'],
          ['I', 'C', 'Q', 'R', 'F'],
          ['M', 'A', 'L', 'C', 'A'],
          ['J', 'T', 'I', 'V', 'E']], "EDUCATIVE"),

        ([['E', 'D', 'X', 'I', 'W'],
          ['P', 'A', 'F', 'M', 'Q'],
          ['I', 'C', 'A', 'S', 'F'],
          ['M', 'A', 'L', 'C', 'A'],
          ['J', 'T', 'I', 'V', 'E']], "PACANS"),

        ([['h', 'e', 'c', 'm', 'l'],
          ['w', 'l', 'i', 'e', 'u'],
          ['a', 'r', 'r', 's', 'n'],
          ['s', 'i', 'i', 'o', 'r']], "warrior"),

        ([['C', 'Q', 'N', 'A'],
          ['P', 'S', 'E', 'I'],
          ['Z', 'A', 'P', 'E'],
          ['J', 'V', 'T', 'K']], "SAVE"),

        ([['O', 'Y', 'O', 'I'],
          ['B', 'Y', 'N', 'M'],
          ['K', 'D', 'A', 'R'],
          ['C', 'I', 'M', 'I'],
          ['Z', 'I', 'T', 'O']], "DYNAMIC"),
    ]
    num = 1

    for i in input:
        print(num, ".\tGrid =", sep="")
        """ 
        debug and see
        """
        for j in range(len(i[0])):
            print("\t\t", i[0][j])
        if i[1] == "":
            print('\n\tWord = ""')
        else:
            print(f"\n\tWord = {i[1]}")
        search_result = word_search(i[0],i[1])
        if search_result:
            print("\n\tSearch result = True! word found")
        else:
            print("\n\tSearch result = False! word could not be found")

        num+=1
        print("-" * 100, "\n")


if __name__ == "__main__":
    main()