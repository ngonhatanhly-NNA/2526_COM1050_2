from typing import List

class Solution_DP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        lis = [1] * n
        
        for i in range (1, n):
            for prev in range (0, i):
                if nums[i] > nums[prev]:
                    lis[i] = max(lis[i], lis[prev] + 1)

        return max(lis)
    
    # O(n^2) and O(n)

class Solution_BinarySearch:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        ans = []
        ans.append(nums[0])

        for i in range (1, n):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                low = 0
                high = len(ans) - 1

                while low < high:
                    mid = low + (high - low) // 2
                    print(low, high, mid)
                    if ans[mid] < nums[i]:
                        low = mid + 1
                    else:
                        high = mid

                ans[low] = nums[i]
            
        return len(ans)

print(Solution_BinarySearch().lengthOfLIS([10, 9, 2, 5, 3, 7, 101]))