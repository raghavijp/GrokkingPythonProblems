def removeInvalidParentheses(s):
    left_remove, right_remove = 0, 0
    result = set()

    for char in s:
        if char == '(':
            left_remove += 1
        elif char == ')':
            if left_remove > 0:
                left_remove -= 1
            else:
                right_remove += 1

    def backtrack(index, open_count, close_count, path, left_remain, right_remain):
        if index == len(s):
            if left_remain == 0 and  right_remain == 0 and open_count == close_count:
                result.add(path)
            return

        char = s[index]

        if char == '(':
            if left_remain > 0:
                backtrack(index + 1, open_count, close_count, path, left_remain - 1, right_remain)

            backtrack(index + 1, open_count + 1, close_count, path + char, left_remain, right_remain)

        elif char == ')':
            if right_remain > 0:
                backtrack(index + 1, open_count, close_count, path, left_remain, right_remain -1)
            if close_count < open_count:
                backtrack(index + 1, open_count, close_count + 1, path + char, left_remain, right_remain)
        else:
            backtrack(index + 1, open_count, close_count, path + char , left_remain, right_remain)

    backtrack(0, 0, 0, '', left_remove, right_remove)
    return list(result)

def main():
    test_cases = [
        "()())()",  # multiple valid results
        "(a)())()",  # includes letters
        ")(",  # all invalid
        "(a(b(c)d)",  # nested unbalanced
        "((()())(()"  # longer unbalanced expression
    ]

    for i, s in enumerate(test_cases, 1):
        res = removeInvalidParentheses(s)
        print(i,"\t Input", s, sep="")
        print("\t Output : ", res)


if __name__ == "__main__":
    main()