def count_occurrences(strings: list[str]) -> list[tuple[str, int]]:
    '''
    takes list of any strings
    returns list of tuples sorted by count of occurrences for each string in descending order
    in the case of the same counts sorting should be done by strings themselves in ascending order
    1-st item of a tuple is a string
    2-st item of a tuple is the count of occurrences
    '''
    occurrences: dict = __getOccurrences(strings)
    items = occurrences.items()
    result:list[tuple[str, int]] = sorted(items, key=lambda item: (-item[1],item[0]))
    return result
def __getOccurrences(strings: list[str]) -> dict:
    result: dict = {}
    for string in strings:
        count = result.get(string, 0)
        result[string] = count + 1
    return result    
    
    