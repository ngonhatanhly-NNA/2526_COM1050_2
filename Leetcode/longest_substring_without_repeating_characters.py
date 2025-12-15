from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using sliding window to track the repetition
        maximum = float('-inf')
        seen = defaultdict(int)
        left = 0
        for right in range (len(s)):
            if s[right] in seen:
                left = seen[s[right]] + 1
            seen[s[right]] = right

            maximum = max(maximum, right - left + 1)
        return maximum