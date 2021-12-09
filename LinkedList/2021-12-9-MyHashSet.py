# 拉链法
class MyHashSet:
    def __init__(self):
        self.buckets=1009
        self.table=[[] for _ in range(self.buckets)]
    
    def hash(self,key): #定义一个较小的数组table,用hash()来求出key应该在数组中出现的位置，但是由于不同的 key 在求完 hash 之后，可能会存在碰撞冲突，所以数组并不直接保存元素，而是每个位置都指向了一条链表（或数组）用于存储元素。
        return key%self.buckets

    def add(self, key: int) -> None:
        hashkey=self.hash(key) #求出key在数组中的位置
        if key in self.table[hashkey]: #如果已经在数组下的链表中了，不做任何操作
            return
        self.table[hashkey].append(key) #不在的话，则添加进去

    def remove(self, key: int) -> None:
        hashkey=self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        hashkey=self.hash(key)
        if key in self.table[hashkey]:
            return True
        else:
            return False
        # 这个if...else...语句可以写成一句：
        # return key in self.table[hashkey] 
        # return 后面的语句为真则返回true，否则返回false



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)