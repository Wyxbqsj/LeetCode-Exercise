# LeetCode-Exercise
力扣刷题争取每日一练，从【字符串】开始进行记录整理
## 目录
#### 1. 字符串：[题解目录](https://github.com/Wyxbqsj/LeetCode-Exercise#%E5%AD%97%E7%AC%A6%E4%B8%B2), [代码目录](https://github.com/Wyxbqsj/LeetCode-Exercise/tree/main/String)
#### 2. 递归：[题解目录](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/README.md#%E9%80%92%E5%BD%92)，[代码目录](https://github.com/Wyxbqsj/LeetCode-Exercise/tree/main/Recursion)
#### 3. 链表：[题解目录](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/README.md#%E9%93%BE%E8%A1%A8)，[代码目录](https://github.com/Wyxbqsj/LeetCode-Exercise/tree/main/LinkedList)
#### 4. 二叉树：[题解目录](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/README.md#%E4%BA%8C%E5%8F%89%E6%A0%91)，[代码目录](https://github.com/Wyxbqsj/LeetCode-Exercise/tree/main/BinaryTrees)



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
<br>（23）[无重复字符的最长字串](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-19-lengthOfLongestSubstring.py)，注意滑动窗口的解法，还有字串和子序列的区别，比如，对于字符串s = "pwwkew"，其无重复字符的最长子串是 "wke"，所以该题答案为3，注意答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
<br>（24）[最长回文串](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-20-longestPalindrome.py)
<br>方法1：[动态规划](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-20-longestPalindrome.py)，暴力解法，将长度为1到len(s)长度的字符串全部判断一遍是不是字符串，最后再找出其中最长的那个。
<br>方法2：[中心扩展法](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-10-21-longestPalindrome.py)，从边界情况（1个字符和2个字符两种边界情况）向外扩展，枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止，此时的回文串长度即为此「回文中心」下的最长回文串长度。我们对所有的长度求出最大值，即可得到最终的答案。
<br>（25）[Z字形变换](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-11-24-convert.py)，难，需要找规律，看看flag的妙用。
<br>（26）字符串转换整数：
<br>[解法一：冗长的暴力判断法](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-11-25-myAtoi.py)，字符串处理的题目往往涉及复杂的流程以及条件情况，如果直接上手写程序，一不小心就会写出极其臃肿的代码。
<br>[解法二：自动机](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-11-28-myAtoi.py)，我们的程序在每个时刻有一个状态 s，每次从序列中输入一个字符 c，并根据字符 c 转移到下一个状态 s'。这样，我们只需要建立一个覆盖所有情况的从 s 与 c 映射到 s' 的表格即可解决题目中的问题。
![image](https://iknow-pic.cdn.bcebos.com/0df431adcbef7609a771da0e3cdda3cc7cd99e2d)
<br>[解法三：解法一的改进](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-11-30-myAtoi.py)，添加一个start变量省去多个if判断句来查看除空格外的第一个字符是什么。
<br>（27）[整数转罗马字符](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-11-29-intToRoman.py)，模拟的方法来解决，用一个字典+一个列表+一重循环即可
<br>（28）电话号码的字母组合：
<br>[解法一：回溯法](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-11-30-letterCombinations.py)，当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。
<br>[解法二：队列](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-11-30-letterCombinations2.py)，比解法一复杂度略低。
<br>（29）[括号生成](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/String/2021-12-1-generateParenthesis.py)，递归式解法

## 递归
（1）[合并两个有序链表](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/Recursion/2021-12-2-mergeTwoLists.py)

## 链表
（1）相交链表：
<br>[解法一：简单用一个visited集合记录](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-3-getIntersectionNode.py)
<br>[解法二：双指针]()
<br>（2）[移除链表元素](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-6-removeElements.py),建立一个dummy node来获得前驱结点，另外巩固了指针相关知识。
<br>（3）[反转链表](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2012-12-6-reverseList.py)，pre,cur,next三个节点来控制。
<br>（4）[回文链表](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-8-isPalindrome.py)，利用快慢指针来找到链表的中点。
<br>（5）[删除链表中的结点](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-9-deleteNode.py),不给头结点，只有待删除的结点，通过交换待删除的结点和他的下一个结点来实现删除（只需交换结点的值即可，甚至不用交换，只需将下一个结点的值保存下来，因为待删除的结点即使节点值交换了最后也会被删除）。
<br>（6）[设计哈希集合](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-9-MyHashSet.py),链地址法：为每个哈希值维护一个链表，并将具有相同哈希值的元素都放入这一链表当中。
![image](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9waWMubGVldGNvZGUtY24uY29tL0ZpZ3VyZXMvNzA1LzcwNV9saW5rZWRfbGlzdC5wbmc?x-oss-process=image/format,png)
<br>（7）[设计哈希映射](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-10-myHashMap.py)，与上一道题的区别在于，存入的是一个键值对，代码用item[]来表示，item[0]是key，item[1]是value。
```
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i,item in enumerate(seasons): #i是索引，item是具体值
  print(i)
  print(item)
print(list(enumerate(seasons)))
# 结果：[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
```
<br>（8）[链表的中间节点](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-11-middleNode.py)，注意两种终止条件，当链表有两个中间节点时，while fast and fast.next返回第二个中间结点；while fast.next and fast.next.next返回第一个中间结点，另附上由一个数组nums，将其转成链表的代码：
```
def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head=ListNode(nums[0])
    cur=head
    for i in range(1,len(nums)):
        cur.next=ListNode(nums[i])
        cur=cur.next
    return head
```
<br>（9）[二进制链表转整数](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-12-getDecimalValue.py)，可以不用求链表的长度，直接遍历求出结果。
<br>（10）[两数相加](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-13-addTwoNumbers.py)，注意在题目这种逆序排列的前提下，补全一个链表无需在头结点前面加值为0的dummy结点，只需在链表为空时，再将头结点变为值为0的dummy结点即可，即：head=ListNode(0)。
<br>（11）删除链表的倒数第N个结点：<br>为了方便，我们在原有链表前面设置一个dummy node，dummy node的好处在于: 当我们是要删除一个结点时，我们可以定位到被删除结点的前置结点，然后将前置结点的后续指 针指向被删除结点的后续结点，则可完成删除。而头结点无前置结点，因此我们用dummy node指向它来控制它的前驱结点。
<br>[方法一：栈](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-14-removeNthFromEnd.py)，遍历链表，将链表中的结点依次入栈，最后弹出第n个结点即可
<br>[方法二：快慢指针](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-14-removeNthFromEnd2.py)，我们设置两个指针，两个指针初始状态都指向dummy node，!!!指针fast先走n步，然后指针fast和指针slow同步往前继续遍历链表，直到fast的后续结点为空，此时指针slow到达被删除结点的前置结点。其实在快慢指针方法中，fast用来控制边界条件，slow用来定位结点。
<br>（12）两两交换链表中的结点：
<br>[方法一：栈](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-15-swapPairs.py)，用一个新链表来控制最后的结果，每次pop()出来都接到新链表上。
<br>[方法二：递归](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-15-swapPairs2.py),学到了链表中交换两个结点的通用操作：
```
# 交换x和y的值：
temp=x; x=y; y=temp
# 交换链表中nodex和nodey：交换链表中的两个点，需要考虑他们的前后节点，也就是考虑四个结点
# 比如原链表是：0->x->y-1
# 交换后：0->y->x->1
temp.next=nodey; nodex.next=nodey.next;nodey.next=nodex
因此上面这段代码中temp就是记录了0这个node，描述了下交换后的链表之间的关系
```
<br>（13）[旋转链表](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-16-rotateRight.py)，学会了利用快慢指针来找链表倒数第k个结点。
<br>（14）[删除链表中的重复元素](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-16-deleteDuplicates.py)，第一道链表题中没有看题解，一次提交就通过的题目！开心！！！
<br>（15）[分隔链表](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-17-partition.py)，一定要将新建的链表尾结点的next设为None，这个和后台的判定程序有关，十分重要。
<br>（16）反转区间内的链表
<br>[方法一：简单方法](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-17-reverseBetween.py)，将中间要反转得部分截取下来，然后反转后再接回去，注意：修改节点当中的next才能修改这个节点指向的下一个节点。last=after只是把after赋值给last,并没有修改指向。
<br>[方法二：一次遍历，不另外写函数](https://github.com/Wyxbqsj/LeetCode-Exercise/blob/main/LinkedList/2021-12-17-reverseBetween2.py)，写这种指针指向交换问题：没有固定的顺序，但一定要能保证变量可以访问到每个节点，不要在换的过程中，有些节点就被漏掉了。


## 二叉树













