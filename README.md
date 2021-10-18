# LeetCode-Exercise
力扣刷题争取每日一练，数组已经做了25道，无更多记录，从【字符串】开始进行记录整理
## 目录
#### 1. 字符串：[题解目录](https://github.com/Wyxbqsj/LeetCode-Exercise#%E5%AD%97%E7%AC%A6%E4%B8%B2), [代码目录](https://github.com/Wyxbqsj/LeetCode-Exercise/tree/main/String)
## 字符串：
<br>（1） [罗马数字转整数](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-6-romanToInt.py)
<br>（2） [最长公共前缀](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-6-longestCommonPrefix.py)
<br>10月6日——暴力循环法，从题目可知：最长公共前缀的最长长度一定是字符串数组中长度最短哪个字符串。首先找出长度最短的字符串str，假如str="abcf"。依次对'abcf'、'abc'、'ab'、'a'进行筛选，判断哪个是所有其他字符串的前缀。
<br>（3）[有效的括号](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-7-isValid.py)
<br>用栈来解决，遇到左括号放入栈顶，遇到右括号，判断与栈顶的左括号是否对应，不对应则为False，对应则将栈顶元素pop出来，直到栈空。！！！精彩的部分：使用哈希表存储每一种括号。哈希表的键为右括号，值为相同类型的左括号。
<br>（4） [实现strStr()函数](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-7-strStr.py)
<br>方法1——字符串切片时间窗，漏洞百出，（一个字母一个字母比较难点在于无法确定开始字母的位置，没想到好办法，卒），用切片的话第一个位置的元素比较容易确定，在haystack[i:i+len(needle)]错了很久，之前写成了haystack[i:len(needle)]，这样的话切片的长度在缩小。
<br>方法2——[Sunday算法求解](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-8-strStr.py),关键点：偏移位用来记录元素的起始位置。两个方法的思路差别：
![image](https://iknow-pic.cdn.bcebos.com/42166d224f4a20a42849b35782529822730ed0cf)
<br>（5）[最后一个单词的长度](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-8-lengthOfLastWord.py)先去除字符串末尾的空格，再反向遍历
<br>反向遍历list两种写法:
```
1)while loop
i=len(list)-1
while i>=0:
  i=i-1

2)for loop
for i in range(len(list)-1,-1,-1):
```
<br>（6）[二进制求和](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-9-addBinary.py)借鉴「列竖式」的方法，末尾对齐，逐位相加。在十进制的计算中「逢十进一」，二进制中我们需要「逢二进一」。学到的两个语法知识：
```
在字符串前补0，如将‘aa’补成长度为5的字符串‘000aa’
s='aa'
s=zfill(5)
倒着输出list或者字符串
str=str[::-1]
```
<br>（7）[验证回文串](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-10-isPalindrome.py)双指针做烂，但是学到了判断字符串是否是空格或数字还是字母的函数：
```
    str.isalnum() 所有字符都是数字或者字母
    str.isalpha() 所有字符都是字母
    str.isdigit() 所有字符都是数字，如果带小数点，则会返回False
    str.isspace() 所有字符都是空白字符、t、n、r
    str.lower() 将字符串转成小写字母
    str.upper() 将字符串转成大写字母
```
<br>（8）[Excel表名称](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-10-convertToTitle.py)
<br>better solution:
```
# 这是一道从1开始的26进制转换题。
# 对于一般性的进制转换题目，只需要不断地对 columnNumbercolumnNumber 进行 % 运算取得最后一位，然后对 columnNumber 进行 / 运算，将已经取得的位数去掉，直到 columnNumber为 0即可。
# 一般性的进制转换题目无须进行额外操作，是因为我们是在「每一位数值范围在 [0,x)」的前提下进行「逢 x进一」。
# 但本题需要我们将从 1 开始，因此在执行「进制转换」操作前，我们需要先对 columnNumber 执行减一操作，从而实现整体偏移。
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        # 10进制 转换为 26进制，A对应1，B对应2,....Z对应26
        while columnNumber > 0:
            # 最右边位为取模运算的结果
            columnNumber -= 1
            # A的ASC码是65，常识a-z：97-122，A-Z：65-90，0-9：48-57
            ans.append(chr(columnNumber%26 + 65)) #先直接用list来存，将ASC码转成字符chr()
            columnNumber //= 26
        return ''.join(ans[::-1]) #输出结果转成字符串的方式，ans[::-1]求ans的倒序输出
```
<br>（9）[Excel表列序号](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-11-titleToNumber.py)特殊的进制转换：将26进制转成10进制。学到的两个函数：
```
ord(c) #将字符c转成ASCII码
chr(i) #将ASCII码i转成字符
```
<br>（10）[同构字符串](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-11-isIsomorphic.py)双映射求解，判断两遍。利用zip()函数同时遍历多个数组
<br>（11）[有效的字母异位词](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-12-isAnagram.py),哈希表求解每个字母出现的次数再比较即可，也可以只求一个字符串中字母出现的次数，再遍历另一个，遇到出现的字母，则对应count-1，直到都为0则返回true，该方法需要的空间更小。
<br>（12）[二叉树的所有路径](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-13-binaryTreePaths.py)千万不要忘记在Debug调试的时候自己把树建好，输入是list，需要将其转为二叉树的类，建树过程代码如下：
```
# 树的结点定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 递归建树
def listcreateTree(rootClass,rootList,i): #输入是rootList，输出是rootClass，当前根节点是i
    if i<len(rootList):
        if rootList[i]==None: #根节点不存在，直接返回空
            return None
        else:
            rootClass=TreeNode(rootList[i]) #赋值当前节点的value
            rootClass.left=listcreateTree(rootClass.left,rootList,2*i+1) #递归建左叉树：输入是rootList,输出是rootClass.left，当前根节点是2*i+1
            rootClass.right=listcreateTree(rootClass.right,rootList,2*i+2) #递归建右叉树：输入是rootList,输出是rootClass.right，当前根节点是2*i+2
            return rootClass #返回当前递推出来的树
    return rootClass #rootList遍历完了，返回整棵树
```
方法1：[DFS](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-13-binaryTreePaths.py)，递归实现，在深度优先搜索遍历二叉树时，我们需要考虑当前的节点以及它的孩子节点。如果当前节点不是叶子节点，则在当前的路径末尾添加该节点，并继续递归遍历该节点的每一个孩子节点。如果当前节点是叶子节点，则在当前路径末尾添加该节点后我们就得到了一条从根节点到叶子节点的路径，将该路径加入到答案即可。
<br>（13）[单词规律](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-14-wordPattern.py),依然是双映射求解，注意从字符串中提取出单词，不需要遍历提取，可以用split()函数：
```
s = "dog cat cat dog"
li = s.split(' ') #将s由空格分开
print(li) #结果输出为['dog','cat','cat','dog']
```
（14）[反转字符串](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-14-reverseString.py)，双指针。
<br>（15）[反转字符串中的元音字母](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-14-reverseVowels.py)，其实不必非要用字典存大小写元音字母，直接用list存，看看遍历到的字母在不在这个list中即可。
<br>（16）[赎金信](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-15-canConstruct.py)，哈希表
<br>（17）[字符串中第一个唯一字符](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-15-firstUniqChar.py)，可直接用counter函数统计字母出现的频数，无需构建哈希表。
<br>（18）[找不同](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-17-findTheDifference.py)
<br>（19）[判断子序列](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-17-isSubsequence.py)
<br>方法1：[双指针贪心法](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-17-isSubsequence.py)
<br>方法2：
<br>（20）[FizzBuzz](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-18-fizzBuzz.py)
<br>（21）[字符串相加](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-18-addString.py)，模拟加法，满十进一。
<br>（22）[最长回文串](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-18-longestPalindrome.py)
