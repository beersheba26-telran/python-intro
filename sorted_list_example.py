from sortedcontainers import SortedList, SortedKeyList
sortedList: SortedList = SortedList(["Apple", "apple", "Apricot"])
print(sortedList) # SortedList(['Apple', 'Apricot', 'apple'])
#no possibility apply case insensitive comparing for SortedList, but only for SortedKeyList
sortedKeyList: SortedKeyList = SortedKeyList(["Apple", "apple", "Apricot"], key= str.lower)
print([s for s in sortedKeyList]) # ['Apple', 'apple', 'Apricot']


