
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            # [ 1, 2, 3, 4, 5]
            print(mid, left, right)
            if not isBadVersion(mid-1):
                left = mid + 1
            else:
                right = mid
            print(mid, left, right)
            print("_____________________-")
        return left

def isBadVersion(version: int):
    bad = [False, False, False, True, True]
    return bad[version]

print(Solution().firstBadVersion(5))