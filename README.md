# LeetCode-Exercise
力扣刷题争取每日一练，数组已经做了25道，无更多记录，从【字符串】开始进行记录整理
#### 1.字符串：
<br>（1）简单题 [2021-10-6罗马数字转整数](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-6-romanToInt.py)
<br>（2）简单题 [2021-10-6最长公共前缀](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-6-longestCommonPrefix.py)
<br>10月6日——暴力循环法，从题目可知：最长公共前缀的最长长度一定是字符串数组中长度最短哪个字符串。首先找出长度最短的字符串str，假如str="abcf"。依次对'abcf'、'abc'、'ab'、'a'进行筛选，判断哪个是所有其他字符串的前缀。
<br>（3）简单题[2021-10-7有效的括号](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-7-isValid.py)
<br>用栈来解决，遇到左括号放入栈顶，遇到右括号，判断与栈顶的左括号是否对应，不对应则为False，对应则将栈顶元素pop出来，直到栈空。！！！精彩的部分：使用哈希表存储每一种括号。哈希表的键为右括号，值为相同类型的左括号。
<br>（4）简单题 [2021-10-7实现strStr()函数](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-7-strStr.py)
<br>10月7日——字符串切片时间窗，漏洞百出，（一个字母一个字母比较难点在于无法确定开始字母的位置，没想到好办法，卒），用切片的话第一个位置的元素比较容易确定，在haystack[i:i+len(needle)]错了很久，之前写成了haystack[i:len(needle)]，这样的话切片的长度在缩小。
<br>10月8日——[Sunday算法求解](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-8-strStr.py),关键点：偏移位用来记录元素的起始位置。两个方法的思路差别：
![image](https://iknow-pic.cdn.bcebos.com/42166d224f4a20a42849b35782529822730ed0cf)
<br>（5）简单题[2021-10-8最后一个单词的长度](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-8-lengthOfLastWord.py)
<br>先去除字符串末尾的空格，再反向遍历
<br>反向遍历list两种写法:
```
1)while loop
i=len(list)-1
while i>=0:
  i=i-1

2)for loop
for i in range(len(list)-1,-1,-1):
```
<br>（6）简单题[2021-10-9二进制求和](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-9-addBinary.py)
<br>借鉴「列竖式」的方法，末尾对齐，逐位相加。在十进制的计算中「逢十进一」，二进制中我们需要「逢二进一」。学到的两个语法知识：
```
在字符串前补0，如将‘aa’补成长度为5的字符串‘000aa’
s='aa'
s=zfill(5)
倒着输出list或者字符串
str=str[::-1]
```
