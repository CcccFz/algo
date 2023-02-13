#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
from typing import List

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans, high, n = 1, intervals[0][1], len(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] >= high:
                high = intervals[i][1]
                ans += 1
        return n-ans
# @lc code=end
s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals([[1,2],[2,3]]))
