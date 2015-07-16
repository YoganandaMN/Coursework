import json
import re
from collections import OrderedDict
import GeneratingJson
def filterData(name,n):
#def fib():
          #n=['MayorMarlene ', ' LowandeChair - Public Safety Committee/Recreationmlowande@jamesburgborough.orgTerm Expires: 12/31/15']
          #yoga=' Tel: 732-521-4946'
          delete_list = ['COUNCIL ','Council Standing ','COUNCIL','Mayor',' Councilman ',' Council Woman ',' Council President ','MayorMarlene ','Councilman','Council President',' Councilwoman ',' Mayor ','Councilwoman ','Council President ','Councilman ','Councilman Donald Applegate','Councilman Thomas Reilly','Council President Michael Gross','Councilman Christine Noble','Councilman Zusette Dato','Mayor: Fred Henry','Mayors Secretary: Stacey Kenndy',' Council President',' Council Vice President',' Councilman',' Councilman',' Councilwoman','Councilwoman','Deputy Mayor',' President',' Vice President',' Mayor','Finance DepartmentGregory Mayers']

          #print n
          #print name
          length=len(n)
          #print length
          #name="sammer"

          try:
                    print "Came indie try"
                    if length>=5:
                    #if n[1] in delete_list:
                              #print "Came inside >5"
                              n[0], n[1] = n[1], n[0]
                              n[2]='.'.join(n[2:5])
                              del n[3:5]
                              n.insert(0,name)
                              #print n

                              #f=n
                              GeneratingJson.AlterData(n)



                    elif length == 2:
                              print "Came inside length 2"
                              for Mail in n:
                                        x=re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',Mail)
                                        if x:
                                                  #mail1=[]
                                                  mail1=x.group()
                                                  mail2=mail1[10:-4]
                                                  n.insert(3,mail2)
                                        date=re.search(r'(\d+/\d+/\d+)',Mail)
                                        if date:
                                                  date1=date.group()
                                                  #print date1
                                                  #n[4]
                                                  #n[3]=mail2
                              n1=n[0]
                              n2=n1[5:]
                              n3=n1[0:5]
                              #print n2,n3
                              n.insert(0,name)
                              n[1]=n3
                              n[2]=n2
                              n[4]=date1
                              #print n
                              GeneratingJson.AlterData(n)
                              #pass
                    elif length == 4:
                              n.insert(0,name)
                              #print n
                              GeneratingJson.AlterData(n)
                    elif length == 3:
                              print "Came inside length 3"
                              n.insert(0,name)
                              m=n[1]
                              m1=n[2]
                              n[1],n[2]=m1,m
                              #n[2]=m
                              #print n
                              GeneratingJson.AlterData(n)



          except :
                    pass
#fib()

