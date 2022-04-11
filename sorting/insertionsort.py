# insertion sort implementation
def insertionsort(arr:list[int]) -> None:
    N = len(arr)

    for i in range(1, N):
        last_element = arr[i]

        j = i - 1
        while j >= 0 and last_element < arr[j]:
            # shift entries to right
            arr[j + 1] = arr[j]
            j -= 1
        
        # all entries greater than last_element is shifted to the right, insert last element to its correct index
        arr[j + 1] = last_element

        

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
insertionsort(test1)
insertionsort(test2)
insertionsort(test3)
insertionsort(test4)

# sanity check
assert (test1 == ans1), f"result: {test1}, expected: {ans1}"
assert (test2 == ans2), f"result: {test2}, expected: {ans2}"
assert (test3 == ans3), f"result: {test3}, expected: {ans3}"
assert (test4 == ans4), f"result: {test4}, expected: {ans4}"
print("INSERTIONSORT SUCCESS!")