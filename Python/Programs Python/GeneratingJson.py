import json
import re
from collections import OrderedDict
def AlterData(n):
          print "came inside GeneratingJson"
          fieldnames=('Township','Role','Name','Address','PhoneNumber','Email','fax','Term Expires')
          listOfData=[None]*8
          #n=['sammer', 'Mayor', 'Marlene ', 'mlowande@jamesburgborough.org', '12/31/15']
          #print n
          #m=re.findall(r'(\w[\w.]+)@([\w.]+)',n)
          #print m

          #print listOfData
          for data in n:
                    p=[]
                    PhoneNo=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',data)
                    if PhoneNo:
                              listOfData[4]=PhoneNo.group()

                              #listOfData[6]=p[1]
                              #print listOfData
                    Email=re.search('[a-zA-Z0-9.!#$%&*+-/=?\^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*',data)
                    if Email:
                              listOfData[5]=Email.group()
                    date=re.search(r'(\d+/\d+/\d+)',data)
                    if date:
                              listOfData[7]=date.group()

                    if len(data)>33 and not (Email or PhoneNo):
                              listOfData[3]=data

          listOfData[0]=n[0]
          listOfData[1]=n[1]
          listOfData[2]=n[2]
          #listOfData[]
          #print "list of data is",listOfData
          def CreateJson():
                    dictionary = OrderedDict(map(None,fieldnames, listOfData))
                    #print dictionary
                    out = json.dumps(dictionary )
                    print out
          CreateJson()

#AlterAlter()


'''
x=re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',n)
print x.group()
y=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',n)
print y.group()
'''