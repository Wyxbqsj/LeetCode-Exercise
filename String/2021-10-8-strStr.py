#Sunday算法
# 目标字符串：haystack
# 模式串：needle
# 当前查询索引：idx，即所求的起始位置
# 算法过程：每次匹配都会从haystack中提取待匹配字符串与needle进行比较：
#          如果一致，返回起始位置idx;
#          若不一致，则查看待匹配字符串的后一位字符c:如果c在needle中，则idx=idx+偏移表[c]；若不在，则除去needle的length外再往后移动一位，idx=idx+len(needle)+1

# !!!偏移表：告诉我们下一步可能匹配需要移动的最小步数
# 作用是存储每一个在“模式串”中出现的字符，在“模式串”中出现的最右位置到尾部的距离+1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def shiftMap(s):
            dic={}
            i=len(s)-1
            while i>=0:
                if not dic.get(s[i]): # 若s[i]的偏移位还没有计算
                    dic[s[i]]=len(s)-i
                    i=i-1
            dic['other']=len(s)+1 #不在s中的字母，直接往后移动
            return dic
        
        dic_needle=shiftMap(needle)
        idx=0

        if len(needle)==0:
            return 0
        if len(haystack)==0 or len(haystack)<len(needle):
            return -1
        while idx+len(needle)<=len(haystack):
            wait=haystack[idx:idx+len(needle)]
            if wait==needle:
                return idx
            else:
                if idx+len(needle)>=len(haystack):#已经查到haystack的底了还不一致，则直接返回-1
                    return -1
                c=haystack[idx+len(needle)]
                if dic_needle.get(c):
                    idx+=dic_needle[c]
                else:
                    idx+=dic_needle['other']
            
        if idx+len(needle)>=len(haystack):
            return -1
        else:
            return idx
        
        #可以写成一句话：return -1 if idx+len(needle)>=len(haystack) else idx

x=Solution()
a=x.strStr("abb","abaaa")
print(a)