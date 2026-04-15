
def pythonicNameRegx() -> str:
    '''
    returns regex for tesing pythonic names match
    Pythonic name may contain only ASCII letters,underscore and digits
    first symbol cannot be a digit
    '''
    return r"[a-zA-Z_]\w*"
def javaNameRegex() -> str:
    '''
    returns regex for tesing Java names match
    Java name may contain only ASCII letters,underscore, $ and digits
    first symbol cannot be a digit
    One $ name is disallowed
    '''
    return r"[a-zA-Z_][\w$]*|\$[\w$]+"
def number_0_300Regex():
    '''
    return matching pattern for string containing number from 0 to 300
    '''
    return r"0|300|[12]\d?\d?|[3-9]\d?"
def ip_octet():
    '''
    return matching pattern for IP octet (number with optional leading zeros from 0 to 255)
    '''
    return r"\d{1,2}|[01]\d\d|2[0-4]\d|25[0-5]"
def ipV4AddressRegex()->str:
    """returns regexp as match pattern of IPv4 address
       comprises of 4 octets separated by dot
       each octet contains 1-3 symbols from 0 to 255
    """ 
    ipOctet = ip_octet()
    return rf"({ipOctet})\.({ipOctet})\.({ipOctet})\.({ipOctet})"
def  mobileIsraelNumberRegex()->str:
    """returns regexp for mobile phone Israel number
       +972- - Israel preffix (not mandatary)
       Operator preffix 0 (only without +972-)
       50,51, 52, 53, 54, 55, 56, 57,58, 59
       optional dash
       7 digits as follows
       xxxxxxx
       xxx-xx-xx
       x-xx-xx-xx
    """  
    return r"(\+972-?|0)5\d-?\d-?\d{2}-?\d{2}-?\d{2}"    
    
    
    