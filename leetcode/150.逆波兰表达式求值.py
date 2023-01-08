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
        for token in tokens:
            if token[-1].isdigit():
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()
                ret = None
                if token == '+':
                    ret = x + y
                elif token == '-':
                    ret = x - y
                elif token == '*':
                    ret = x * y
                elif token == '/':
                    ret = int(x / float(y))                
                stack.append(ret)
        return stack[0]
        
# @lc code=end
s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
