def countAndMerge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    print(n1, n2)
    left = arr[l:m +1]
    right = arr[m+1:r+1]

    res = 0
    i, j, k = 0, 0, l

    while i < n1 and j  < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i +=1
        else:
            arr[k] = right[j]
            j +=1 
            res += (n1 -i)
        k +=1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k +=1
    while j < n2:
        arr[k] = right[j]
        j +=1
        k +=1
    print(arr)
    return res

def countInv(arr, l, r):
    res = 0
    if l < r:
        # Binary search to separate 
        m = (r + l) // 2
        # recursively count inversions in the left and right halves
        # Divide and conquer, break problem into smaller subproblems, solve each ò the smaller sub individually
        # divide first, conquer, and merge 
        res += countInv(arr,l, m)
        res += countInv(arr, m + 1, r)
        # T(n) = aT(n/b) + f(n) n: size of input, a nmber of subproblems, n/b size of each sub
        print(res)
        print(r, l)
        res += countAndMerge(arr, l, m, r)

    return res
# Using merge sort to count , for each sort res += 
def inversionCount(arr):
    return countInv(arr, 0, len(arr) - 1)

arr = [8, 4, 2, 1]
print(inversionCount(arr))