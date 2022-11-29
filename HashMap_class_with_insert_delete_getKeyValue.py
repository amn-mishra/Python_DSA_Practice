'''This is our class of Dictionary and we are going to create hashmap we will
 insert key , delete dey , size of hashmap , get_value_of_key , these functions
but it takes O(n) time all operatoin :

we want good complexity so we will maintain load factor which is n/b < 0.7  n= number of entities ,b = size of our bucket
to maintain the load factor we take help of rehashing in which we create another double size bucket and copy values
from one to another '''


class Mapnode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map :
    def __init__(self):
         self.bucketsize = 10
         self.bucket = [None for i in range(self.bucketsize)]
         self.count = 0

    def size(self):
        return self.count

    def getBucketIndex(self, hc):
        return (abs(hc)%(self.bucketsize))

    def getvalue(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def removeKey(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        pre = None
        while head is not None:
            if head.key == key:
                if pre is None:
                    self.bucket[index]  = head.next
                else:
                    pre.next = head.next
                self.count -= 1
                return head.value
            pre = head
            head = head.next
        return "not find "


    def insert(self,key,value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key :
                head.value = value
                return
            head = head.next

        head = self.bucket[index]
        newMapNode = Mapnode(key, value)
        newMapNode.next = head
        self.bucket[index] = newMapNode
        self.count += 1


aman = Map()
aman.insert("xyz", 120)
aman.insert("abc", 10)
aman.insert("dfd", 450)
aman.insert("weec", 10)
aman.insert("ad", 54)
print(aman.removeKey("dfd"))
print(aman.getvalue("dfd"))
print(aman.size())









