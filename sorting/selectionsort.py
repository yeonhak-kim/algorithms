# selection sort implementation
def selectionsort(arr:list[int]) -> None:
    N = len(arr)

    for i in range(N):
        # index i: target index (selected index) to find the sorted value
        min_index = i
        for j in range(i, N):
            if arr[min_index] > arr[j]:
                # update minimum index
                min_index = j
        
        # swap entries
        arr[i], arr[min_index] = arr[min_index], arr[i]
    


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
selectionsort(test1)
selectionsort(test2)
selectionsort(test3)
selectionsort(test4)

# sanity check
assert (test1 == ans1), f"result: {test1}, expected: {ans1}"
assert (test2 == ans2), f"result: {test2}, expected: {ans2}"
assert (test3 == ans3), f"result: {test3}, expected: {ans3}"
assert (test4 == ans4), f"result: {test4}, expected: {ans4}"
print("SELCTIONSORT SUCCESS!")