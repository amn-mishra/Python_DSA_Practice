'''importing the heapq lib for making the min heap and max heap'''
import heapq
'''This is for creating the Min heap and use the functions '''
lis = [3, 5, 2, 7, 4, 9]

heapq.heapify(lis)  #it will make the min Heap takes 1 argument
print(lis)

heapq.heappush(lis,1) #it will insert the value into our min heap accordingly return nothing
print(lis)

print(heapq.heappop(lis)) #it will remove the min value from the min heap and return that value as well
print(lis)

heapq.heapreplace(lis,10) #it will change the first element by given element then create again the min heap accordingly
print(lis)
print("we have seen all fuctions ! \n")

#_________________________________________________________________________________________________________________________________
'''This is for creating the Max heap and use the functions '''

lis = [3, 6, 7, 2, 9, 5]

heapq._heapify_max(lis) #for creating the Max heap of the list
print(lis)

print(heapq._heappop_max(lis)) #for removing the max value which is at 1st position
print(lis)

heapq._heapreplace_max(lis, 0 ) #same as above but here we will do as per max heap
print(lis)

#for inserting see carefully
lis.append(100)
heapq._siftdown_max(lis, 0, len(lis) - 1) # see argument(list , starting index or array , last index )
print(lis)