class Solution:
    def reverseWords(self,str):
        # 三步翻转法：
        # 1. 将str转成list
        # 2. 先将整个list翻转一次：abc de -> ed cba
        # 3. 再将每个单词单独翻转一次：ed cba -> de abc
        # 4. 最后将list转成str
        def reverse(l,begin,end):
            a,b=begin,end
            while a<b:
                l[a],l[b]=l[b],l[a]
                a+=1
                b-=1
        
        lstr=list(str)
        length=len(lstr)
        reverse(lstr,0,length-1)
        i=0
        start=0
        while i<length:
            if lstr[i]==' ':
                reverse(lstr,start,i-1)
                start=i+1
            if i==length-1:
                reverse(lstr,start,i)
            i+=1
        return "".join(lstr)

# 注意：当reverse()函数写得同reverseWords()函数并列时,此时他为类内函数，调用需要用：self.reverse()

x=Solution()
a=x.reverseWords("the sky is blue")
print(a)
