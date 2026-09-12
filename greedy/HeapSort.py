def heapify(nums, n , i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right

    if largest != i:
        nums[i] , nums[largest] = nums[largest] , nums[i]
        heapify(nums,n,largest)

def sortArray(nums):
    n = len(nums)

    for i in range(n//2 -1, -1, -1):
        heapify(nums,n,i)

    for i in range(n-1, 0, -1):
        nums[0] , nums[i] = nums[i] , nums[0]
        heapify(nums, i , 0)

    return nums


def main():
    test_cases = [
        [5, 2, 3, 1],
        [9, -3, 5, 0, -10, 8],
        [2, 2, 1, 3, 1],
        [10, -10, 9, -9, 8, -8],
        [4, -1, -1, 2, -2, 0],
    ]

    for i, nums in enumerate(test_cases, start=1):
        print(f"{i}.\tnums: {nums}")
        sorted_nums = sortArray(nums.copy())  # use copy() to keep original intact
        print(f"\tOutput: {sorted_nums}")
        print("-" * 100)


if __name__ == "__main__":
    main()

"""


Approach	        Time Complexity	    Space Complexity
Heap Sort	        O(n log n)	        O(1)
Bubble Sort     	O(n^2)	            O(1)
Insertion Sort	    O(n^2)	            O(1)
Merge Sort	        O(n log n)	        O(n)
Quick Sort	        O(n log n)	        O(log n)

Time Complexity Comparison

Heap Sort, Merge Sort, and Quick Sort all have average time complexities of O(n log n), making them efficient for large datasets.
Heap Sort achieves this in-place, making it space-efficient.
Merge Sort, while also O(n log n), requires O(n) space for the temporary arrays used during the merge process.
Quick Sort’s performance can degrade to O(n^2) in the worst case but is generally faster in practice due to smaller constant factors.
Bubble Sort and Insertion Sort have time complexities of O(n^2), making them less efficient for large datasets.


Space Complexity Comparison

Heap Sort and Bubble Sort are in-place sorting algorithms with a space complexity of O(1), making them very space-efficient.
Insertion Sort, while also in-place, tends to perform poorly on larger datasets.
Merge Sort requires additional space (O(n)) for temporary arrays used during the merge process, making it less space-efficient than the in-place sorting algorithms.
Quick Sort has a space complexity of O(log n) due to the stack space required for recursive calls, which is better than Merge Sort but not as good as the in-place algorithms.
"""