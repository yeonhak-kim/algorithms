# bubble sort implmentation
def bubblesort(arr: list[int]) -> None:
    N = len(arr)

    for i in range(N):
        swapped = False
        for j in range(N - 1 - i):
            if arr[j] > arr[j + 1]:
                # swap entries
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            
        if not swapped:
            # sorting complete
            break



# test cases
test1 = [1,2,3,4,5,6]               # sorted  = [1,2,3,4,5,6]
ans1 = [1,2,3,4,5,6]
 
test2 = [2,1,3,7,2,4,5]             # sorted = [1,2,2,3,4,5,7]
ans2 = [1,2,2,3,4,5,7]

test3 = [6,4,2,1]                   # sorted = [1,2,4,6]
ans3 = [1,2,4,6]

test4 = [1,-1,-4,54,2,7,3,9,-33]    # sorted = [-33,-4,-1,1,2,3,7,9,54]
ans4 = [-33,-4,-1,1,2,3,7,9,54]

# run bubblesort
bubblesort(test1)
bubblesort(test2)
bubblesort(test3)
bubblesort(test4)

# sanity check
assert (test1 == ans1), f"result: {test1}, expected: {ans1}"
assert (test2 == ans2), f"result: {test2}, expected: {ans2}"
assert (test3 == ans3), f"result: {test3}, expected: {ans3}"
assert (test4 == ans4), f"result: {test4}, expected: {ans4}"
print("BUBBLESORT SUCCESS!")