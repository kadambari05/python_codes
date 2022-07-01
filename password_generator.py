import random

U1=chr(random.randint(65,90))
U2=chr(random.randint(65,90))
L1=chr(random.randint(96,122))
L2=chr(random.randint(96,122))
l1=chr(random.randint(0,15))
l2=chr(random.randint(0,15))
s1=chr(random.randint(33,41))
def shuffle(string):
    templist=list(string)
    random.shuffle(templist)
    return ''.join(templist)
password=(U1+U2+L1+L2+l1+l2+s1)
password=shuffle(password)
print(password)
f=open("store_password.txt",'a')
f.write(" " + str(password))
