from sortedcontainers import SortedDict
monthsNamesDict = {}
monthsNamesSortedDict = SortedDict()
monthsNamesDict.setdefault(1, "Jan")
monthsNamesSortedDict.setdefault(1, "Jan")
################################
monthsNamesDict.setdefault(12, "Dec")
monthsNamesSortedDict.setdefault(12, "Dec")
################################
monthsNamesDict.setdefault(10, "Oct")
monthsNamesSortedDict.setdefault(10, "Oct")
print("months in dict", monthsNamesDict)
print("months in SortedDict", monthsNamesSortedDict)
