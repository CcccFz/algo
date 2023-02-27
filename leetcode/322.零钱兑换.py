#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from typing import List
# @lc code=start
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        state = [0] + [math.inf] * amount
        for coin in coins:
            for x in range(coin, amount+1):
                state[x] = min(state[x], state[x-coin]+1)
        return -1 if state[-1] == math.inf else state[-1]
# @lc code=end
s = Solution()
print(s.coinChange([1,2,5], 11))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))