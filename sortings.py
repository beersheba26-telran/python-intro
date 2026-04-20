def bsearch(sortedList: list, search_key)-> int:
    
    '''
    O[LogN]
    returns index of search_key if it exists in the sortedList
    returns -(insort_index + 1) if it doesn't exist
    example: sortedList: [10, 20, 40], search_key: 5, returns -1, seacrh_key: 25, returns -3, search_key: 20, returns 1
    Hints: leftindex, rightindex
    '''
    left: int = 0
    right: int = len(sortedList) - 1
    middle: int = (left + right) // 2
    while left <= right and sortedList[middle] != search_key :
        if search_key < sortedList[middle] : 
            right = middle - 1
        else :
            left = middle + 1
        middle = (right + left) // 2
    return middle if left <= right else -(left + 1) 

def insort(sortedList: list, item) :
    '''
    inserts into sortedList item keeping sorted order
    '''
    index = bsearch(sortedList, item)
    if index < 0: index = -(index + 1)
    sortedList.insert(index, item)
      