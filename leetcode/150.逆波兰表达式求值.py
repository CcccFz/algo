#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

from typing import List

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c[-1].isdigit():
                stack.append(int(c))
            else:
                y = stack.pop()
                x = stack.pop()
                ret = 0
                if c == '+':
                    ret = x + y
                elif c == '-':
                    ret = x - y
                elif c == '*':
                    ret = x * y
                else:
                    ret = int(x/float(y))
                stack.append(ret)
        return stack[0]
        
# @lc code=end
s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))