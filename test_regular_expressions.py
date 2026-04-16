import regular_expressions as regex
from unittest import TestCase
import re
class TestRegEx(TestCase):
    def test_pythonic_name_true(self):
        pythonicNameRX = regex.pythonicNameRegx()
        self.assertTrue(re.fullmatch(pythonicNameRX,"__"))
        self.assertTrue(re.fullmatch(pythonicNameRX,"abc"))
        self.assertTrue(re.fullmatch(pythonicNameRX,"d1"))
        self.assertTrue(re.fullmatch(pythonicNameRX,"d_5"))
        self.assertTrue(re.fullmatch(pythonicNameRX,"_123"))
        self.assertTrue(re.fullmatch(pythonicNameRX,"B1"))
    def  test_pythonic_name_false(self): 
        pythonicNameRX = regex.pythonicNameRegx() 
        self.assertFalse(re.fullmatch(pythonicNameRX, " _")) 
        self.assertFalse(re.fullmatch(pythonicNameRX, "1ax")) 
        self.assertFalse(re.fullmatch(pythonicNameRX, "a-f")) 
        self.assertFalse(re.fullmatch(pythonicNameRX, "a*t")) 
    def test_java_name_true(self):
        javaNameRX = regex.javaNameRegex()
        self.assertTrue(re.fullmatch(javaNameRX,"$1")) 
        self.assertTrue(re.fullmatch(javaNameRX,"abc1$"))     
        self.assertTrue(re.fullmatch(javaNameRX,"_lmn"))   
        self.assertTrue(re.fullmatch(javaNameRX,"__")) 
        self.assertTrue(re.fullmatch(javaNameRX,"$$"))  
    def test_java_name_false(self):
        javaNameRX = regex.javaNameRegex() 
        self.assertFalse(re.fullmatch(javaNameRX, "$"))  
        self.assertFalse(re.fullmatch(javaNameRX, "1i"))  
        self.assertFalse(re.fullmatch(javaNameRX, " abc"))  
        self.assertFalse(re.fullmatch(javaNameRX, "a-$"))  
        self.assertFalse(re.fullmatch(javaNameRX, "lm*y"))  
    def test_number_0_300_true(self):
        number_0_300_RX = regex.number_0_300Regex() 
        self.assertTrue(re.fullmatch(number_0_300_RX, "0"))   
        self.assertTrue(re.fullmatch(number_0_300_RX, "300"))   
        self.assertTrue(re.fullmatch(number_0_300_RX, "30"))   
        self.assertTrue(re.fullmatch(number_0_300_RX, "1"))   
        self.assertTrue(re.fullmatch(number_0_300_RX, "15"))   
        self.assertTrue(re.fullmatch(number_0_300_RX, "51"))   
        self.assertTrue(re.fullmatch(number_0_300_RX, "199"))   
        self.assertTrue(re.fullmatch(number_0_300_RX, "290")) 
    def test_number_0_300_false(self): 
        number_0_300_RX = regex.number_0_300Regex() 
        self.assertFalse(re.fullmatch(number_0_300_RX, "00"))     
        self.assertFalse(re.fullmatch(number_0_300_RX, "301"))     
        self.assertFalse(re.fullmatch(number_0_300_RX, "500"))     
        self.assertFalse(re.fullmatch(number_0_300_RX, "3000"))     
        self.assertFalse(re.fullmatch(number_0_300_RX, "11*"))     
        self.assertFalse(re.fullmatch(number_0_300_RX, " 3"))     
        self.assertFalse(re.fullmatch(number_0_300_RX, "-33"))
    def test_ip_octet_true(self):
        ipOctetRX = regex.ip_octet()
        self.assertTrue(re.fullmatch(ipOctetRX, "0"))
        self.assertTrue(re.fullmatch(ipOctetRX, "00"))        
        self.assertTrue(re.fullmatch(ipOctetRX, "000"))        
        self.assertTrue(re.fullmatch(ipOctetRX, "255"))        
        self.assertTrue(re.fullmatch(ipOctetRX, "200"))        
        self.assertTrue(re.fullmatch(ipOctetRX, "199")) 
        self.assertTrue(re.fullmatch(ipOctetRX, "99")) 
        self.assertTrue(re.fullmatch(ipOctetRX, "9")) 
        self.assertTrue(re.fullmatch(ipOctetRX, "29")) 
    def test_ip_octet_false(self):
        ipOctetRX = regex.ip_octet()    
        self.assertFalse(re.fullmatch(ipOctetRX, "0000"))
        self.assertFalse(re.fullmatch(ipOctetRX, "256"))
        self.assertFalse(re.fullmatch(ipOctetRX, "299"))
        self.assertFalse(re.fullmatch(ipOctetRX, "299"))
        self.assertFalse(re.fullmatch(ipOctetRX, "2 9"))
        self.assertFalse(re.fullmatch(ipOctetRX, "-100"))
        self.assertFalse(re.fullmatch(ipOctetRX, "0010"))
    def test_ipV4_true(self) :
        ipV4addressRX = regex.ipV4AddressRegex()
        self.assertTrue(re.fullmatch(ipV4addressRX, "0.0.0.0")) 
        self.assertTrue(re.fullmatch(ipV4addressRX, "0.01.002.000")) 
        self.assertTrue(re.fullmatch(ipV4addressRX, "000.1.249.59")) 
        self.assertTrue(re.fullmatch(ipV4addressRX, "250.255.199.9"))
    def test_ipV4_false(self) :
        ipV4addressRX = regex.ipV4AddressRegex()
        self.assertFalse(re.fullmatch(ipV4addressRX, "0.0.0")) 
        self.assertFalse(re.fullmatch(ipV4addressRX, "0000.0.0.2"))  
        self.assertFalse(re.fullmatch(ipV4addressRX, "0.0.0.256"))
        self.assertFalse(re.fullmatch(ipV4addressRX, "0.0 0.2"))
        self.assertFalse(re.fullmatch(ipV4addressRX, "0.0.0.280"))
        self.assertFalse(re.fullmatch(ipV4addressRX, "0.0.0.0001"))
        self.assertFalse(re.fullmatch(ipV4addressRX, "0.0.0. 190"))
        self.assertFalse(re.fullmatch(ipV4addressRX, "0.0.0.+1"))
        self.assertFalse(re.fullmatch(ipV4addressRX, "0.0.0.a"))
    def test_mobile_israel_true(self):
        mobileIsraelNumberRX = regex.mobileIsraelNumberRegex()
        self.assertTrue(re.fullmatch(mobileIsraelNumberRX, "+972-54-1234567"))
        self.assertTrue(re.fullmatch(mobileIsraelNumberRX, "+972-541234567")) 
        self.assertTrue(re.fullmatch(mobileIsraelNumberRX, "+972-541234567"))
        self.assertTrue(re.fullmatch(mobileIsraelNumberRX, "059123-45-67")) 
        self.assertTrue(re.fullmatch(mobileIsraelNumberRX, "054-1-23-45-67"))
        self.assertTrue(re.fullmatch(mobileIsraelNumberRX, "0571-23-45-67"))
    def test_mobile_israel_false(self):
        mobileIsraelNumberRX = regex.mobileIsraelNumberRegex()
        self.assertFalse(re.fullmatch(mobileIsraelNumberRX, "+972-054-1234567"))
        self.assertFalse(re.fullmatch(mobileIsraelNumberRX, "+972-54-1-234-567")) 
        self.assertFalse(re.fullmatch(mobileIsraelNumberRX, "+972-54123456"))
        self.assertFalse(re.fullmatch(mobileIsraelNumberRX, "059123-45-677")) 
        self.assertFalse(re.fullmatch(mobileIsraelNumberRX, "054-1-2-3-45-67"))
        self.assertFalse(re.fullmatch(mobileIsraelNumberRX, "0571-23-45-6-7"))
        self.assertFalse(re.fullmatch(mobileIsraelNumberRX, "054-1-23-4567"))     
             
        
               
          
          
          