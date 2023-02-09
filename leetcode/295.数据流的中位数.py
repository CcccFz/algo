#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
            if len(self.left) - len(self.right) > 1:
                heapq.heappush(self.right, -heapq.heappop(self.left))
        else:
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left):
                heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0]+self.right[0]) / 2
        return -self.left[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian()) # 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian()) # 3