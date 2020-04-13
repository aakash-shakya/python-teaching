
# bubble sort 
# selection sort

# binary search



arr = [23,34,54,12,67,45,87,34,87,45,23,12,36,94,26]



def BubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1,n):
            if (array[i]>array[j]):
                temp = array[i]
                array[i]=array[j]
                array[j]=temp

                #arr[i],arr[j]=arr[j],arr[i]
    return array


# sorted_arr = BubbleSort(arr)
# print(sorted_arr)      

def SelectionSort(array):
    n = len(array)
    
    for i in range(n):
        pos = i
        for j in range(i+1,n):
            if (array[i]>array[j]):
                pos = j

                array[i],array[j] = array[pos],array[i]

    return array

#binary search
def BinarySearch(arr,target):
    n = len(arr)
    sorted = SelectionSort(arr)
    

    left=0
    right = n-1

    found = False

    while(left<=right):
        mid = int((left+right)/2)
        if target not in arr:
            print("not found")
            break
            
        elif target==sorted[mid]:
            found = True
            #print("found")
            break               #### never forget to break here other wise the program goes to infinite loop

        elif target > sorted[mid]:
            left = mid
            #print('greater')

        elif target<sorted[mid]:
            right = mid
            #print('lesser')
        

    if (found==True):
        print("found target is in {} index".format(mid))

BinarySearch(arr,7)


arr = [12,23,34,45,56,67,78,89,90,343,345,256,567,345,567,4]

#sorting with steps