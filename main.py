import re
import regular_expressions
import sys
text:str = '''
Service is running on the server with public IP 54.10.8.33, DB server has private IP 172.10.15.20,
DB Backup server has private IP 172.10.30.40
Watch-dog monitoring server has private IP 172.10.88.15
'''
ip_pattern = re.compile(regular_expressions.ipV4AddressRegex())
matchObjectsIter = ip_pattern.finditer(text) #iterator of groups
print("size of iterator", sys.getsizeof(matchObjectsIter))
allIpAddresses: list[str] = [mo.group() for mo in matchObjectsIter]
print(allIpAddresses)
print("size of list is ", sys.getsizeof(allIpAddresses))

