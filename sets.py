def remove_repeated(lst: list)->list:
    '''
    returns list with no repeated items
    '''
    helper: set = set() #creating the empty set
    return [item for item in lst if  item not in helper and not helper.add(item)]

def max_negative_representive(lst: list[int]) -> int:
    '''
    returns maximal positive number having its negative representive
    if no one with negative representive, returns -1
    Algorithm complexity O[N]
    '''
    
    
