class Solution:
    def numTrees(self, n: int) -> int:
        # Using dynamic program to track the math problem
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        # Find the root of the node, the node can be multiple to root
        # [1, 1, 2, 1 + 2 + 2]
        for nodes in range (2, n + 1):
            for root in range (1, nodes  + 1):
                left_sub = dp[root - 1]
                right_sub = dp[nodes - root]

                dp[nodes] += left_sub * right_sub

        return dp[n]