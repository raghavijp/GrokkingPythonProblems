def find_tribonacci_num(num):
    if num < 3:
        return 1 if num else 0

    first_num = 0
    second_num = 1
    third_num = 1

    for _  in range(3, num+1):
        temp = first_num + second_num + third_num
        first_num = second_num
        second_num = third_num
        third_num = temp

    return third_num


def main():
    n = [4, 5, 25, 17, 19]
    for i in range(len(n)):
        print(f"\t Number:", n[i], end="")
        print(f"\t Tribonacci value:", find_tribonacci_num(n[i]))
        print("*" * 100)


if __name__ == "__main__":
    main()