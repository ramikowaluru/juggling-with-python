from array import array


# searching an element in the array
# search for the value 4
def linear_search_array(arr_size,arr,search_element):
    for i in range(arr_size):
        if arr[i]==search_element:
            print("The value is found at the index ", i)
            return
    print("element not found")

def get_the_max_element(arr, arr_size):
    max_elem=None
    if arr:
        max_elem=arr[0]
    else:
        return max_elem
    for i in range(2,arr_size, 1):
        if arr[i]>max_elem:
            max_elem=arr[i]

    return max_elem

if __name__ == '__main__':
    arr = array('i', [i * i for i in range(4)])
    arr_size = 4
    print(arr)

    # accessing value at index 3
    print("value at third index is ", arr[2])
    # accessing at the index 2
    print("value at second index is ", arr[1])
    # slicing the array
    print("slicing the array from the index 2 to 3", arr[1:3])

    # accessing from the end
    print("last element of the array is", arr[-1])
    # except last two
    print("except last two elements of the array", arr[:-2])

    # set value at an index
    arr[0] = 9
    print("value at the index 0 of the array is", arr[0])

    # finding an element in the array
    linear_search_array(arr_size, arr, 4)

    print("biggest element in the array is ",get_the_max_element(arr, arr_size))
