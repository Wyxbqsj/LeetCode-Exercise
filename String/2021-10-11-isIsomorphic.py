#暴力法超时
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        si=0
        for si in range(len(s)):
            sj=si+1
            for sj in range(len(s)):
                if s[si]==s[sj]:
                    if t[si]==t[sj]:
                        continue
                    else:
                        return False
                if t[si]==t[sj]:
                    if s[si]==s[sj]:
                        continue
                    else:
                        return False
        return True
'''   
# 双映射！只验证一个方向是不可以的，s到t的map是唯一的，t到s的map也是唯一的
# 对于 s 到 t 的映射，我们同时遍历 s 和 t ，假设当前遇到的字母分别是 c1 和 c2 。
# 如果 map[c1] 不存在，那么就将 c1 映射到 c2 ，即 map[c1] = c2。
# 如果 map[c1] 存在，那么就判断 map[c1] 是否等于 c2，也就是验证之前的映射和当前的字母是否相同。
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def strMap(s,t):
            strmap={}
            for c1,c2 in zip(s,t): # 利用zip()函数同时遍历两个list
                if not strmap.get(c1):
                    strmap[c1]=c2
                else:
                    if strmap[c1]==c2:
                        continue
                    else:
                        return False
            return True
        if strMap(s,t) and strMap(t,s):
            return True
        else: 
            return False
       

x=Solution()
a=x.isIsomorphic("badc","baba")
print(a)
            

