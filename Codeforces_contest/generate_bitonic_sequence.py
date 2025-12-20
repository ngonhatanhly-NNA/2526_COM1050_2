""" Given intergers n, l, r -> generate Bitonic Sequence ( a sequence that must be strictly 
increasing at first and then strictly decresing of length n from the integers in the range
[L, r] such that the first element is the maximum. IF it is not possible to create such a sequence -< return -1)"""

# We can see that if length <= (l - r) * 2 + 1 -> all possible, just move

from collections import deque

def bitonicArray(n, l, r):
    if n > (r - l) * 2 + 1:
        return [-1]

    dq = deque()
    dq.append(r-1)

    i = r
    while i >= l and len(dq) < n:
        dq.append(i)
        i -= 1
    
    i = r - 2
    while i >= l and len(dq) < n:
        dq.appendleft(i)
        i -= 1

    return list(dq)