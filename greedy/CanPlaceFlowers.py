def canPlaceFlowers(arr):
    n = len(arr)
    count = 0

    for i in range(n-1,0,-1):
        if arr[i] == 0:
            left = i ==0 or arr[i-1] == 0
            right = i == n-1 or arr[i+1] == 0

            if left and right:
                arr[i] = 1
                count += 1

                if count == n:
                    return True

    ###When count becomes equal to or greater than n,
    # it means you have planted enough flowers to satisfy the requirement.
    ###So, returning count >= n means:
    ###TRUE: You managed to plant all n flowers without breaking the no-adjacent-flowers rule.
    ###FALSE: You couldn’t plant all n flowers under the given constraints.

    return count >=n

