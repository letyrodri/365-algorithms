from math import floor

def swap(arr, i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def bubble_sort2(arr):
    n = len(arr)

    for k in range(0, n):
        for i in range(0, n-1):
            j = i+1
            a = arr[i]
            b = arr[j]

            if a > b:
                swap(arr, i, j)

def bubble_sort(arr):
    n = len(arr)
    sw = -1

    while(sw != 0):
        sw = 0
        for i in range(0, n-1):
            j = i+1
            a = arr[i]
            b = arr[j]

            if a > b:
                swap(arr, i, j)
                sw += 1

    return arr
                
if __name__ == '__main__':
    
    arr = [1,4,3,2,6,7,5]
    bubble_sort(arr)           
    print(arr)

