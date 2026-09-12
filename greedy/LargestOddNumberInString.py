def largest_odd_number(test_case):
    for i in range (len(test_case)- 1, -1,-1):
        if int(test_case[i]) % 2 == 1:
            return test_case[:i+1]
    return ""


def main():
    test_cases = [
        "345679",  # Example with multiple odd digits
        "357",  # Example with all odd digits
        "2468",  # Example with no odd digit
        "5",  # Example with a single odd digit
        "74",  # Example with one odd and one even digit
        "4597680"  # Example with even digits at the end
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = largest_odd_number(test_case)
        print(f"{i}.\tnum: {test_case}")
        print(f"\tResult: {result}")
        print("-" * 100)

main()