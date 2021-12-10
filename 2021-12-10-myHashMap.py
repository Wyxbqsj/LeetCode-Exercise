class MyHashMap:

    # 若还像上一道构建哈希集合，取模之后存数组，链接同样的hashkey的number不可行，因为需要通过key来返回value
    # 因此这道题与MyHashSet的唯一区别在于，存储的是键值对(key,value)，而非key本身
    def __init__(self):
        # 分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。由此我们取1009，是因为 1009 是大于 1000 的第一个质数。
        self.buckets=1009
        self.table=[[] for _ in range(self.buckets)]   
        
    def hash(self,key):
        return key%self.buckets

    def put(self, key: int, value: int) -> None: # 比如key=100
        hashkey=self.hash(key) # hashkey=100
        for item in self.table[hashkey]: # 在序号100的这个桶里的所有item
            if item[0]==key: # 如果有item的key等于传进来的值
                item[1]=value #则将该item的value设为传进来的value
                return
        self.table[hashkey].append([key,value]) #如果没有这样的一个item，就append上来


    def get(self, key: int) -> int:
        hashkey=self.hash(key)
        for item in self.table[hashkey]:
            if item[0]==key:
                return item[1]
        return -1


    def remove(self, key: int) -> None:
        hashkey=self.hash(key)
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        for i,item in enumerate(self.table[hashkey]): #因此i得到的是索引即第几个item，而item则返回的是具体的键值对
            if item[0]==key: # 若item的key是要删除的那个的话
                self.table[hashkey].pop(i) # 则在第hashkey个桶中将第i个item删掉
             



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)