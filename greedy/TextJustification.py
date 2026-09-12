def getWords(i, words, maxWidth):
    current_line=[]
    curr_length = 0

    while i < len(words) and curr_length + len(words[i]) <= maxWidth:
        current_line.append(words[i])
        curr_length += len(words[i]) + 1
        i += 1

    return current_line


def join(line, delimiter):
    if not line:
        return ""
    res = line[0]

    for i in range(1, len(line)):
        res += delimiter + line[i]
    return res


def createLine(line, i, words, maxWidth):
    baselength = -1
    for word in line:
        baselength += len(word) + 1

    extra_spaces = maxWidth - baselength

    if len ==1 or i == len(words):
        res = join(line , " ")
        res += " " * extra_spaces
        return res

    word_count = len(line) - 1
    spaces_per_word = extra_spaces // word_count
    needs_extra_spaces = extra_spaces % word_count

    for j in range(needs_extra_spaces):
        line[j] += " "

    for j in range(word_count):
        line[j] += " " * spaces_per_word

    return join(line, " ")


def fulljustify(words, maxWidth):
    ans = []
    i = 0

    while i < len(words):
        current_line = getWords(i, words, maxWidth)
        i += len(current_line)
        ans.append(createLine(current_line,i,words,maxWidth))

    return ans

if __name__ == "__main__":
    test_cases = [
        ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        ["Uneven", "space", "distribution", "matters", "a", "lot", "here"],
        ["Many", "tiny", "words", "fit", "into", "a", "single", "line"],
        ["To", "be", "or", "not", "to", "be"],
        ["Artificial", "Intelligence", "and", "Creativity"]
    ]

    widths = [16, 18, 38, 10, 25]

    for idx, words in enumerate(test_cases):
        print(f"{idx + 1}.\tInput words: {words}")
        print(f"\tMax Width: {widths[idx]}\n")

        result = fulljustify(words , widths[idx])

        print("\tOutput lines:")
        for line in result:
            print(f'\t"{line}" ({len(line)} chars)')
        print("-" * 100)