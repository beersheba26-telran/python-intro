from sortedcontainers import SortedSet
sortedSetNoKey: SortedSet[str] = SortedSet(["Apple", "apple", "Application", "Apricot"])
print([s for s  in sortedSetNoKey]) # ['Apple', 'Application', 'Apricot', 'apple']
sortedSetKey: SortedSet[str] = SortedSet(["apple", "Apple",  "Application", "Apricot"], key=str.lower)
print([s for s  in sortedSetKey])