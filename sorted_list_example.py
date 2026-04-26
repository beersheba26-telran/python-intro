from sortedcontainers import SortedList
sortedList: SortedList = SortedList([10, 20, 30, 20, 40,  20])
print(sortedList) # printing out whole list in sorted order
print(sortedList[sortedList.bisect_left(20):sortedList.bisect_right(20)])# printing out all 20
sortedList.remove(20)# removing one 20
del sortedList[sortedList.bisect_left(20):sortedList.bisect_right(20)] #removing all 20
print(sortedList[sortedList.bisect_left(20):sortedList.bisect_right(20)])# printing out all 20

