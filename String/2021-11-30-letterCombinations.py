'''
回溯法：复杂度略高
'''
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        dic={'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','k','l'],
             '6':['m','n','o'],
             '7':['p','q','r','s'],
             '8':['t','u','v'],
             '9':['w','x','y','z']}
        res=[]
        def backtrack(combination,strs):
            if len(strs)==0:
                res.append(combination)
            else:
                for letter in dic[strs[0]]:
                    backtrack(combination+letter,strs[1:])
        backtrack('',digits)
        return res


x=Solution()
a=x.letterCombinations('23')
print(a)     