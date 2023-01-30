#
# @lc app=leetcode.cn id=1206 lang=python3
#
# [1206] 设计跳表
#

# @lc code=start
class Skiplist:

    def __init__(self):


    def search(self, target: int) -> bool:


    def add(self, num: int) -> None:


    def erase(self, num: int) -> bool:



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end
skiplist = Skiplist()
skiplist.add(1)
skiplist.add(2)
skiplist.add(3)
print(skiplist.search(0))
skiplist.add(4)
print(skiplist.search(1))
print(skiplist.erase(0))
print(skiplist.erase(1))
print(skiplist.search(1))