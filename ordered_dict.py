from collections import OrderedDict


orderedDict: OrderedDict = OrderedDict()
args = [1, 2, 3, 4, 5]
for arg in args:
    orderedDict[arg] = arg ** 2
print(orderedDict) 
orderedDict.move_to_end(1) 
orderedDict.popitem(last=False)
print(orderedDict)  