#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from typing import List
# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_i, g_n = 0, len(g)
        s_i, s_n = 0, len(s)
        while g_i < g_n and s_i < s_n:
            if g[g_i] > s[s_i]:
                s_i += 1
                continue
            g_i += 1
            s_i += 1
        return g_i
# @lc code=end
s = Solution()
print(s.findContentChildren([1,2,3], [1,1]))
print(s.findContentChildren([1,2], [1,2,3]))