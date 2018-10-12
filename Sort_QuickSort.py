


def quick_sort(p_list, l, r):
    if l < r:
        mid = partition(p_list, l, r)
        quick_sort(p_list, l, mid-1)
        quick_sort(p_list, mid+1, r)

def partition(p_list, l, r):
    last = p_list[r]
    i = l - 1
    for j in range(l, r):
        if p_list[j] <= last:
            i += 1
            p_list[i], p_list[j] = p_list[j], p_list[i]
    p_list[i+1], p_list[r] = p_list[r], p_list[i+1]
    return i+1


if __name__ == '__main__':
    p_list = [1,4,2,3,5,2]
    quick_sort(p_list, 0, len(p_list)-1)
    print(p_list)

    
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
