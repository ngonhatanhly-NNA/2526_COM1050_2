class Solution:
    def nextGreaterElements(self, nums):
        # In circulare, so run n * 2
        n = len(nums)
        st = []
        res = [-1] * n

        for i in range (n * 2):
            while st and nums[i % n] > nums[st[-1]]:
                idx = st.pop()
                res[idx] = nums[i % n]
            if i < n:
                st.append(i)

        return res