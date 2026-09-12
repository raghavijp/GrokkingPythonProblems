def maximumSwaps(num):
    num_string = list(str(num))
    n = len(num_string)
    max_digit_index,index1, index2 = -1

    for i in range(n-1,0,-1):
        if max_digit_index == -1 or num_string[i] > num[max_digit_index]:
            max_digit_index = i
        elif num_string[i] < num_string[max_digit_index]:
            index1 = i
            index2 = max_digit_index

    if index1 != -1 and index2!= -1:
        num_string[index1] , num_string[index2] = num_string[index2] , num_string[index1]

    return int("".join(num_string))



def main():
    num = [4121, 87654, 1643, 123, 14]

    for i in range(len(num)):
        print(i+1,".\tNumber",num[i])
        print("\n\tLargest Number after swapping:", maximumSwaps(num[i]))
        print("*" * 100)

if __name__== main():
    main()