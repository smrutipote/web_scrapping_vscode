import re
import urllib
import pandas as pd
from urllib.request import urlopen

url='https://www.summet.com/dmsi/html/codesamples/addresses.html'

exdata=urlopen(url)
data=exdata.read().decode()

req=re.sub('(<li>)','',data)
#print(req)
reqq1=re.sub('(</li>)','',req)
#print(reqq1)
reqq=re.sub('<br/>','  ',reqq1)
#print(reqq)
list=reqq.split('\n')
num_list=[]
pin_list=[]
def web(list):
    for line in list:
        number = re.findall('[(][0-9]{3}[)][ ][0-9]{3}[-][0-9]{4}',line)
        pin=re.findall('[A-Z]{2}[ ][0-9]{5}',line)
        if number:
            num_list.append(number)
        else:
            num_list.append(' ')
        if pin:
            pin_list.append(pin)
        else:
            pin_list.append(' ')
    print(pin_list)
    print(num_list)
    return num_list,pin_list
phone,pincode=web(list)
print(len(phone))
print(len(pincode))

if __name__ == '__main__':
    print('this is phone\n',phone)
    print('this is pincode\n', pincode)