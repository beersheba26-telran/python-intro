from bisect import bisect_left, bisect_right
numbers = [10, 20, 20, 20, 20, 30 ,40]
print(bisect_left(numbers, 20)) # 1 (before most left 20)
print(bisect_right(numbers, 20)) # 5 (after most right 20)
print (bisect_left(numbers, 35)) #6 (index for insorting 35 to keep order)
print (bisect_right(numbers, 35)) #6 (index for insorting 35 to keep order)
'''
3 following statements for printing numbers in the closed range [30-40]
'''
min = bisect_left(numbers, 30)
max = bisect_right(numbers, 40)
print(numbers[min:max]) # [30, 40]