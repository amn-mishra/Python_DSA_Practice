'''This is our class of Dictionary and we are going to create hashmap we will
 insert key , delete dey , size of hashmap , get_value_of_key , these functions
but it takes O(n) time all operatoin :

we want good complexity so we will maintain load factor which is n/b < 0.7  n= number of entities ,b = size of our bucket
to maintain the load factor we take help of rehashing in which we create another double size bucket and copy values
from one to another

all operation and also concept of rehash
'''


class Mapnode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map :
    def __init__(self):
         self.bucketsize = 5
         self.bucket = [None for i in range(self.bucketsize)]
         self.count = 0

    def rehash(self):
        temp = self.bucket
        self.bucket = [None for i in range(2*self.bucketsize)]
        self.bucketsize = 2*self.bucketsize
        self.count = 0

        for head in temp:
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next

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

    def LoadFactor(self):
        return self.count/self.bucketsize

    def insert(self, key, value):
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

        LoadFactor = self.count/self.bucketsize
        if LoadFactor >= 0.7:
            self.rehash()



aman = Map()
for i in range(10):
    aman.insert('abc'  +str(i), i+1)
    print(aman.LoadFactor())

print()
for i in range(10):
    print("abc"+str(i+1)+":" ,aman.getvalue( 'abc'+str(i)))





