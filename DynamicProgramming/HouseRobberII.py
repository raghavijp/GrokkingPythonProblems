def find_max_value_robbery_helper(money):
    lookup_array = [0 for _ in range(len(money)+1)]
    lookup_array[0] = 0 # base case
    lookup_array[1] = money[0] # only one house to rob

    for i in range(2, len(money)+1):
        lookup_array[i] = max(money[i-1] + lookup_array[i-2] , lookup_array[i-1])

    return lookup_array[-1]

def find_max_value_robbery(arr):
    if len(arr) == 0 or arr is None:
        return 0

    if len(arr) == 1:
        return arr[0]

    return max(find_max_value_robbery_helper(arr[:-1]), find_max_value_robbery_helper(arr[1:]))


def main():
    inputs = [[2, 3, 2], [1, 2, 3, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [7, 4, 1, 9, 3], []]
    
    for i in range(len(inputs)):
        print(f"\t Given Array", inputs[i])
        print(f"\t Maximum Value of Robbery: ", find_max_value_robbery(inputs[i]))
        print("_"*100)
        
    
if __name__ == "__main__":
    main()