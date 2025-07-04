def Sort(arr, low, high):
    pivot=arr[low]
    i=low+1
    j=high
    while True:
        while i <= j and arr[i] <=pivot:
            i+=1

        while i<= j and arr[j] >=pivot:
            j-=1

        if i<=j:
            arr[i],arr[j] = arr[j],arr[i]

        else:
            break

    arr[low] , arr[j] = arr[j] , arr[low]
    return j


def QuickSort(arr,low,high):
    if low< high:
        pivot=Sort(arr, low, high)
        QuickSort(arr, low, pivot-1)
        QuickSort(arr, pivot+1, high)

arr=[23,345,11,23,11,544,35,35,4567,11,42,756,422,90,74]
QuickSort(arr,0,14)
print(arr)