from collections import Counter


def largest_palindrome(num):
    occurances = Counter(num)

    first_half=[]
    midlle = ""

    for digit in range(9,-1,-1):
        digit_char = str(digit)

        if digit_char in occurances:
            digit_count = occurances[digit_char]

            num_pairs = digit_count // 2

            if num_pairs:
                if not first_half and not digit:
                    occurances["0"] = 1
                else:
                    first_half.append(digit_char * num_pairs)

            if digit_count % 2 and not midlle:
                midlle = digit_char

    if not midlle and not first_half:
        return "0"

    return "".join(first_half + [midlle] + first_half[::-1])


def main():
    numbers = ["00001","1234287","9876545367282","000000", "146"]

    for i in range(len(numbers)):
        print(i + 1, '.', '\tGiven number: "', numbers[i], '"', sep='')
        result = largest_palindrome(numbers[i])
        print('\n\tThe largest palindromic number: "', result, '"', sep='')
        print('-' * 100)
        
if __name__ == '__main__':
    main()