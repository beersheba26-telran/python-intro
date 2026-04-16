import re
import regular_expressions
text:str = '''
Service is running on the server with public IP 54.10.8.33, DB server has private IP 172.10.15.20,
DB Backup server has private IP 172.10.30.40
Watch-dog monitoring server has private IP 172.10.88.15
'''
ip_pattern = re.compile(regular_expressions.ipV4AddressRegex())
matchObj: re.Match[str] = ip_pattern.search(text)
if( matchObj):
    print("public IP of the server is ",matchObj.group())
    print("first octet of the public IP is ", matchObj.group(1))
    print("all separate octets of the public Ip is ", list(matchObj.groups())[:-1])
backupIndex = text.index("Backup")
matchObj = ip_pattern.search(text, backupIndex) 
if (matchObj):
    print("private IP of the Backup server is ",matchObj.group())
    print("first octet of the private IP of the Backup server is ", matchObj.group(1))
    print("all separate octets of the private IP of the Backup server is ", list(matchObj.groups())[:-1])
      
