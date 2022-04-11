# quick sort implementation (recursive)
def quicksort(arr: list[int], start: int, end: int) -> None:
    if start < end:
        # parition data
        partitioned_index = partition(arr, start, end)
        # repeat for left and right partitions
        quicksort(arr, start, partitioned_index - 1)
        quicksort(arr, partitioned_index + 1, end)
    

def partition(arr: list[int], start: int, end: int) -> int:
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:

        # iterate start (left -> right) until arr[start] > pivot
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        # iterate end (right -> left) until arr[end] < pivot
        while arr[end] > pivot:
            end -= 1
        
        if start < end:
            # swap start-entry and end-entry
            arr[start], arr[end] = arr[end], arr[start]
    
    # swap pivot with end-index entry (place pivot at the right place)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    # return partitioned index
    return end


# test cases
test1 = [1,2,3,4,5,6]               # sorted  = [1,2,3,4,5,6]
ans1 = [1,2,3,4,5,6]

test2 = [2,1,3,7,2,4,5]             # sorted = [1,2,2,3,4,5,7]
ans2 = [1,2,2,3,4,5,7]

test3 = [6,4,2,1]                   # sorted = [1,2,4,6]
ans3 = [1,2,4,6]

test4 = [1,-1,-4,54,2,7,3,9,-33]    # sorted = [-33,-4,-1,1,2,3,7,9,54]
ans4 = [-33,-4,-1,1,2,3,7,9,54]

# run selectionsort
quicksort(test1, 0, len(test1) - 1)
quicksort(test2, 0, len(test2) - 1)
quicksort(test3, 0, len(test3) - 1)
quicksort(test4, 0, len(test4) - 1)

# sanity check
assert (test1 == ans1), f"result: {test1}, expected: {ans1}"
assert (test2 == ans2), f"result: {test2}, expected: {ans2}"
assert (test3 == ans3), f"result: {test3}, expected: {ans3}"
assert (test4 == ans4), f"result: {test4}, expected: {ans4}"
print("QUICKSORT SUCCESS!")