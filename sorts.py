import math

###########   BINARY SEARCH ###########
def binary_search(arr,v):
    return bin_s(arr,0, len(arr)-1,v)

def bin_s(arr,l,r,v):
    if r>=l:
        mid = math.floor(l + (r -l)/2)
        if arr[mid] == v:
            return mid
        elif arr[mid] < v:
            return bin_s(arr,mid+1,r,v)
        else:
            return bin_s(arr,l,mid-1,v)
    else:
        return -1
    



###### M.S. #############3

def mergeSort(arr):
    if len(arr) > 1:
        mid = math.floor(len(arr)/2)
        # splits array into left and right
        L = arr[:mid]
        R = arr [mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # es el equivalente al merge()
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        # revisa los subarrays por elementos sobrantes
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        return arr
        

############  Q.S. ############


def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


############# 






