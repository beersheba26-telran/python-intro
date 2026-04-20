lst: list = [13, 2, 100, 17, -1, -30, 8]
print(sorted(lst, key=lambda x: x % 2))
# result from line 2 is [2, 100, -30, 8, 13, 17, -1]
# write sorting statement to get the following result:
[-30, 2, 8, 100, 17, 13, -1]
print(sorted(lst, key=lambda x: (x % 2, -x if x % 2 else x) ))