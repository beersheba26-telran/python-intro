import re
import regular_expressions
text:str = '''
Service is running on the server with public IP 54.10.8.33, DB server has private IP 172.10.15.20,
DB Backup server has private IP 172.10.30.40
Watch-dog monitoring server has private IP 172.10.88.15
'''
ip_pattern = re.compile(regular_expressions.ipV4AddressRegex())
matches = ip_pattern.findall(text) #list of tuples with groups
#FIXME
allIpAddresses: list[str] = [".".join(tpl) for tpl in matches]
print(allIpAddresses)
