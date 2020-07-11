import string
import random

def fun():
    
    p_length = int(input())
    
    s1 = string.ascii_letters
    s2= string.punctuation
    s3 = string.digits
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    random.shuffle(s)
    
    passwd = ("".join(s[0:p_length]))
    print(passwd)
    

fun()