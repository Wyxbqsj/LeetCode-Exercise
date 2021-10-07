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
