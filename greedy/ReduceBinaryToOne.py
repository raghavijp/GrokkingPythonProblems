def num_steps(str):
    length = len(str)
    steps = 0
    c = 0

    for i in range(length - 1, 0 , -1):
        digit = int(str[i]) + c
        if digit % 2 == 1:
            steps +=2
            c = 1
        else:
            steps +=1

    return steps + c

def main():
    strings = [
        "1011",
        "111",
        "100",
        "1",
        "10"
    ]

    i =0

    for s in strings:
        print(i + 1, ".\tstr: ", s, sep="")
        print("\n\tsteps: ", num_steps(s), sep="")
        print("-" * 100)
        i+=1


if __name__ == "__main__":
    main()