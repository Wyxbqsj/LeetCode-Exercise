#字符串第3题
#用栈来解决，遇到左括号放入栈顶，遇到右括号，判断与栈顶的左括号是否对应，不对应则为False，对应则将栈顶元素pop出来，直到栈空
class Solution:
    def isValid(self, s):
        left=[]
        dic={')':'(',']':'[','}':'{'} #精妙处：使用哈希表存储每一种括号。哈希表的键为右括号，值为相同类型的左括号。
        for i in s:
            if i=='(' or i=='[' or i=='{':
                left.append(i)
            if i==')' or i==']' or i=='}':
                if len(left)==0:
                    return False
                elif left[-1]==dic[i]:
                    left.pop()
                else:
                    return False
        if len(left)==0:
            return True
        else:
            return False

x=Solution()
a=x.isValid("}")
print(a)
        