import re
import regular_expressions

text: str = '''
Service is running on the server with public ip 54.10.8.33, DB server has private IP 172.10.15.20.
DB Backup server has private IP 172.10.30.40 .
Watch-dog monitoring server has private IP 172.10.88.15.
'''


ip_pattern = re.compile(regular_expressions.ipV4AddressRegex())
matchObj = ip_pattern.search(text)
while matchObj is not None:
    print(matchObj.group())
    matchObj = ip_pattern.search(text, matchObj.end())

backupIndex = text.index("Backup")
matchObj2 = ip_pattern.search(text, backupIndex)
if matchObj2 is not None:
    print(f"DB Backup server IP is: {matchObj2.group()}")