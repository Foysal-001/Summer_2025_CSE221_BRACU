def merge_sort(s):
    if len(s)<=1:
        return s
    

    midpoint=len(s)//2

    left=s[:midpoint]
    right=s[midpoint:]

    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left, right)



def merge(left, right):
    new_list=[]
    i,j=0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i+=1

        else:
            new_list.append(right[j])
            j+=1

    new_list.extend(left[i:])
    new_list.extend(right[j:])
    return new_list

arr=[1,2,3,4,5,6,2,4,5,45,11,23,1,34,1,234,1,3434,12,23,1,42,5,4,13,45,2,4,2,5,4,4,24,46,2323,23]
print(merge_sort(arr))
