'''Program of min priority Queue:
we are using array as a tree : and each element of array has 2 things value and priority
for example = pq = [ nodehas(value,priority), nodehas(value,priority), nodehas(value,priority)...etx ]
    child1Index = 2*parentIndex +1
    child2Index = 2*parentIndex + 2
    parentIndex = (childIndex - 1 )//2
percolateUP when insertion  : always insert in the last of array i.e append
percolateDown when deletion : always remove top of the tree or first index of array

we are implimenting all functions 
1)getMin  2)getsize  3)isempty  4)insert  5)delele '''


class priorityQueueNode:
    def __init__(self,value, priority ):
        self.priority = priority
        self.value = value

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def getMin(self):
        if self.isEmpty() is True :
            return None
        return self.pq[0].value

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize() == 0
    def __percolateUp(self):
        childIndex = self.getSize() -1
        while childIndex > 0 :
            parentIndex = (childIndex - 1 )//2
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex] , self.pq[childIndex] = self.pq[childIndex] , self.pq[parentIndex]
            else:
                break
    def insert(self, value, priority):
        print("inserting value:",value,"with priority",priority)
        pqNode = priorityQueueNode(value,  priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        parentIndex = 0
        leftChildIndex = 2*parentIndex + 1
        rightChildIndex = 2*parentIndex + 2
        while leftChildIndex < self.getSize():
            minChildIndex = parentIndex
            if self.pq[leftChildIndex].priority < self.pq[parentIndex].priority:
                minChildIndex = leftChildIndex
            if rightChildIndex < self.getSize():
                if self.pq[minChildIndex].priority > self.pq[rightChildIndex].priority:
                    minChildIndex = rightChildIndex
            if minChildIndex == parentIndex:
                break
            self.pq[minChildIndex] , self.pq[parentIndex]  = self.pq[parentIndex] , self.pq[minChildIndex]
            parentIndex = minChildIndex
            leftChildIndex = 2*parentIndex + 1
            rightChildIndex =  2*rightChildIndex + 2
    def remove(self):
        if self.isEmpty() :
            return
        ele = self.pq[0].value
        '''for implimentation i am taking this value otherwise no need to write like this'''
        causePriority = self.pq[0].priority
        self.pq[0] = self.pq[self.getSize() -1]
        self.pq.pop()
        self.__percolateDown()
        return ele , causePriority #can remove this second one not needed  just showing :)

a = PriorityQueue()
print("_______________inserting the value:___________________________\n")
'''insert tha value with the priority and this is min priority Queue means it will always keep min value at the top of the tree or array'''
a.insert(10,5)
a.insert(30,1)
a.insert(50,4)
a.insert(90,2)
a.insert(80,7)
a.insert(60,3)

print("\nNote This time minimum priority value is  :",a.getMin())
print("\n_______________Now Removing according to the priority:__________\n")

for i in range(a.getSize()):
    print("removing value with priority ",a.remove())

print(a.isEmpty())
print(a.getSize())