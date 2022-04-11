# merge sort impementation (recursive: divide-and-conquer)
def mergesort(arr: list[int]):
    if len(arr) > 1:
        mid = len(arr)//2

        # partition left-half and right-half arrays
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # sort left-half and right-half arrays
        mergesort(left_arr)
        mergesort(right_arr)

        # merge left-half and right-half into arr
        i = j = idx = 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[idx] = left_arr[i]
                i += 1
            else:
                arr[idx] = right_arr[j]
                j += 1
            idx += 1
        
        # merge remaining left-arr
        while i < len(left_arr):
            arr[idx] = left_arr[i]
            i += 1
            idx += 1
        
        # merge remaining right-arr
        while j < len(right_arr):
            arr[idx] = right_arr[j]
            j += 1
            idx += 1



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
mergesort(test1)
mergesort(test2)
mergesort(test3)
mergesort(test4)

# sanity check
assert (test1 == ans1), f"result: {test1}, expected: {ans1}"
assert (test2 == ans2), f"result: {test2}, expected: {ans2}"
assert (test3 == ans3), f"result: {test3}, expected: {ans3}"
assert (test4 == ans4), f"result: {test4}, expected: {ans4}"
print("MERGESORT SUCCESS!")
            

