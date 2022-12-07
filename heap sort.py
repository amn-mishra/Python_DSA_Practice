def downheapify(arr, i, n):
    parentIndex = i
    leftchidIndex = 2 * parentIndex + 1
    rightchildIndex = 2 * parentIndex + 2
    while leftchidIndex < n:
        miniChildIndex = parentIndex
        if arr[parentIndex] > arr[leftchidIndex]:
            miniChildIndex = leftchidIndex
        if rightchildIndex < n:
            if arr[miniChildIndex] > arr[rightchildIndex]:
                miniChildIndex = rightchildIndex

        if miniChildIndex == parentIndex:
            return

        arr[parentIndex], arr[miniChildIndex] = arr[miniChildIndex], arr[parentIndex]
        parentIndex = miniChildIndex
        leftchidIndex = 2 * parentIndex + 1
        rightchildIndex = 2 * parentIndex + 2


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        downheapify(arr, i, n)

    for j in range(n - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        downheapify(arr, 0, j)
    return arr.reverse()


arr = [1,1,2,6,5,7,3,14,42,11,22,1,9,8,6,2,2,3,4]
heapSort(arr)
print(*arr)