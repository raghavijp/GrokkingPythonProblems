def backtrackSplit(s, start, seen):
    if start == len(s):
        return 0

    max_count = 0

    for end in range (start+1 , len(s)+1):
        sub_string = s[start:end]
        if sub_string not in seen:
            seen.add(sub_string)
            max_count = max(max_count , 1 + backtrackSplit(s, end, seen))
            seen.remove(sub_string)

    return max_count

def max_unique_split(s):
    seen = set()
    return backtrackSplit(s,0,seen)


def main():
    test_cases = [
        "ababccc",
        "aba",
        "abcabc",
        "aabbcc",
        "abcdef"
    ]

    for idx, s in enumerate(test_cases, start=1):
        print(f"{idx}.\tInput string: '{s}'")
        result = max_unique_split(s)
        print(f"\tMaximum unique splits: {result}")
        print("-" * 100)

if __name__ == '__main__':
    main()