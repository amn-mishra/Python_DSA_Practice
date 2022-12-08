import heapq
__________________________________________________________________________________________
'''K largest element in arr'''
def kLargest(lst, k):
    ansArr = []
    for i in range(k):
        heapq.heappush(ansArr, lst[i])

    for i in range(k, len(lst)):
        if ansArr[0] < lst[i]:
            heapq.heappop(ansArr)
            heapq.heappush(ansArr, lst[i])
    return ansArr
# Main Code
lst = [1,29,4,3,30,5,23,7]
k = 4 # enter the value how many largest do you need
ans = kLargest(lst, k)
print(*ans, sep='\n')
__________________________________________________________________________________________
'''K smallest element in arr'''
def kSmallest(lst, k):
    maxHeap = []
    heapq.heapify(maxHeap)

    for i in range(k):
        heapq.heappush(maxHeap, -1*lst[i]) #add first k element to max heap by negating element :) awesome bro 
    for i in range(k, len(lst)):
        if -1*lst[i] > maxHeap[0]:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -1*lst[i])
    ansArr = [val* -1 for val in maxHeap]
    return ansArr

lst = [2,4,5,8,1,9,3,7]
k = 4
ans = kSmallest(lst, k)
ans.sort()
print(ans)


