import csv
import re
from Tkinter import Tk
from tkFileDialog import askopenfilename
import string
#Altering For CranburyTownship.csv and BropgsouthRiver

def alterCsv():
          def modifyReadFIle(data):
                    if data[1] in memberslist:
                              data[0], data[1]=data[1],data[0]
                              hello = [x.strip(' ') for x in data]
                              hello.insert(0,TownName)

                              with open(TownshipName,'ab') as f:
                                        writer=csv.writer(f)
                                        writer.writerow(hello)

                    hello.insert(0,TownName)
                    print hello
                              #print data
          def ModifyAndPrint(ch):
                    print "inside ModifyAndPrint"
                    chh=ch[2]
                    st1=chh.strip('[')
                    st2=st1.strip(']')
                    st3=st2.strip("'")
                    finaldata=''.join(ch[0:2]),st3
                    hello = [x.strip(' ') for x in finaldata]
                    '''
                    with open(TownshipName,'ab') as f:
                              writer=csv.writer(f)
                              writer.writerow(hello)
                    '''
                    print hello

          duplicate=[]
          memberslist=['COUNCIL','COUNCIL ',' Committee Member',' Mayor','Mayor','Deputy Mayor','Liaison to: Planning Board Seat 2','Liaison to: Business and Professional Association','NAME & E-MAIL LINK ','Council Standing ']
          memberslist1=['COUNCIL','COUNCIL ','Mayor']
          Tk().withdraw()
          ReadFile="CranburyTownship.csv"
          filename=askopenfilename()
          print filename
          file=str(filename.split('/')[-1])
          print file
          name=file.split('.')
          rr=re.findall('[A-Z][^A-Z]*', name[0])
          print rr
          TownName=" ".join(rr)
          TownName
          TownshipName="New"+name[0]+".csv"
          with open (file,'r') as inFile:
                    handler=csv.reader(inFile)
                    count=0
                    for data in handler:
                              if data:
                              #print data
                                        count+=1
                                        #print count
                                        try:
                                                  data1=[]
                                                  data1=data
                                                  if data[0] in memberslist or data[1] in memberslist:
                                                            #print data
                                                            if file==ReadFile:
                                                                      modifyReadFIle(data)
                                                                      pass

                                                            else:
                                                                      if data[0] in memberslist1:


                                                                      #print data
                                                                                ls=[]
                                                                                for items in data:
                                                                                          if items is not ' ':
                                                                                                    ls.append(items)
                                                                                #print ls
                                                                                                    #print items

                                                                                chunks=[ls[x:x+3] for x in xrange(0, len(ls), 3)]
                                                                                ch=chunks[0]
                                                                                print ch
                                                                                ModifyAndPrint(ch)
                                                                                ch1=chunks[1]
                                                                                ModifyAndPrint(ch1)
                                                                                ch2=chunks[2]
                                                                                ModifyAndPrint(ch2)
                                                  else:
                                                            #print data
                                                            if file==ReadFile:
                                                                      if count==1:
                                                                                ls=['TownshipName','Department','Name','PhoneNumber','Extension']
                                                                                print ls
                                                                      elif count==2:
                                                                                PhoneNo=str(data[1])
                                                                                PhoneNo=PhoneNo.strip('[')
                                                                                PhoneNo=PhoneNo.strip(']')
                                                                                PhoneNo=PhoneNo.strip()



                                                                                #pass
                                                                      else:
                                                                                PNo=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',str(data))
                                                                                if PNo:
                                                                                          PhoneNo=PNo.group()

                                                                                          #print data
                                                                                          if len(data)==3:
                                                                                                    data[-1],data[-2]=data[-2],data[-1]
                                                                                                    data.insert(0,TownName)
                                                                                                    with open(TownshipName,'ab') as f:
                                                                                                              writer=csv.writer(f)
                                                                                                              writer.writerow(data)
                                                                                                    #print data
                                                                                                    print data
                                                                                          elif len(data)>3:
                                                                                                    data[-3],data[-2]=data[-2],data[-3]
                                                                                                    data[-1],data[-2]=data[-2],data[-1]
                                                                                                    data.insert(0,TownName)
                                                                                                    with open(TownshipName,'ab') as f:
                                                                                                              writer=csv.writer(f)
                                                                                                              writer.writerow(data)
                                                                                                    print data
                                                                                                    #print data

                                                                                else:
                                                                                          #print data
                                                                                          if len(data)>2:
                                                                                                    data[-1],data[-2]=data[-2],data[-1]
                                                                                                    data.insert(-1,PhoneNo)
                                                                                                    data.insert(0,TownName)
                                                                                                    with open(TownshipName,'ab') as f:
                                                                                                              writer=csv.writer(f)
                                                                                                              writer.writerow(data)
                                                                                                    #print data
                                                                                                    print data
                                                                                          else:
                                                                                                    data.insert(-1,PhoneNo)
                                                                                                    data.insert(0,TownName)
                                                                                                    with open(TownshipName,'ab') as f:
                                                                                                              writer=csv.writer(f)
                                                                                                              writer.writerow(data)
                                                                                                    #print data
                                                                                                    print data







                                                            else:
                                                                      pass





                                        except:
                                                  pass





alterCsv()