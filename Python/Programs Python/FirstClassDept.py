import json
import re
from collections import OrderedDict
import GeneratingJson
def filterData(name,n):
#def filterData():
          #n=['Sandra Bohinski', ' Borough Clerk ', ' 51 Main Street', ' Helmetta', ' NJ 08828', ' Tel: 732-521-4946 ext. 100 Fax: 732-605-9466']
          #print n
          length=len(n)
          try:
                    if length == 6:
                              st=n[2]
                              st+=n[3]
                              st+=n[4]
                              print len(st)

                              del n[2:5]
                              n.insert(2,st)
                              s=n[3].split(" ")
                              n[3]=s[2]
                              n.insert(4,s[4])
                              #n[4]=s[4]
                              n.insert(5,s[6])
                              #s1=s[5]+s[6]
                              #n[5]=s1
                              print n



          except :
                    pass

#filterData()