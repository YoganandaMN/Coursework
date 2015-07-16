import csv
import string
import re
from Tkinter import Tk
from tkFileDialog import askopenfilename
def ToRemoveDuplicateValues():
          def SplitName(line1):
                    l=['Council']
                    ALPHA=['a-zA-Z']
                    #print "Came inside SplitName"
                    #print line1
                    count=0
                    data=line1[0]
                    data1=line1[1]
                    #print data1


                    #print data
                    data11=data1.split(':')
                    if len(data11)>1:
                              #print "Inside data1"
                              line1[1]=data11[0]
                              line1.insert(2,data11[1])

                              line1[1],line1[2]=line1[2],line1[1]
                              print line1
                              with open(TownshipName,'ab') as f:
                                        writer=csv.writer(f)
                                        writer.writerow(line1)
                              #print ("\n")

                    else:

                              data2=data1.split('-')
                              if len(data2)>1:
                                        #print "inside data2"
                                        #print data2
                                        line1[1]=data2[0]
                                        line1.insert(2,data2[1])
                                        line1[1],line1[2]=line1[2],line1[1]
                                        with open(TownshipName,'ab') as f:
                                                  writer=csv.writer(f)
                                                  writer.writerow(line1)
                                        print line1

                                        #print ("\n")


                    if data in l:
                              line11=line1[1]
                              #print line11
                              r=re.findall('[A-Z][a-z]*', line11)
                              if len(r)==3:
                                        r1=r[0]
                                        r2=r[1]+r[2]
                                        line1[1]=r1
                                        line1.insert(2,r2)
                                        line1[1],line1[2]=line1[2],line1[1]
                                        print line1
                                        with open(TownshipName,'ab') as f:
                                                  writer=csv.writer(f)
                                                  writer.writerow(line1)
                              else:
                                        r1=r[0]+r[1]
                                        r2=r[2]+r[3]
                                        line1[1]=r1
                                        line1.insert(2,r2)
                                        line1[1],line1[2]=line1[2],line1[1]
                                        with open(TownshipName,'ab') as f:
                                                  writer=csv.writer(f)
                                                  writer.writerow(line1)
                                        print line1









          Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
          filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
          file=filename.split('/')[-1]
          print file
          line1=[]
          name=file.split('.')
          findlist=['City Hall Address:','South Amboy Fire Department','Enterprise Snorkel Fire Company','Independence Fire Company','Mechanicsville Fire Company','Progressive Fire Company','Protection Fire Company','Chief Darren Lavigne']
          TownshipName="New"+name[0]+".csv"

          #inFile = open(file,'r')


          with open (file,'r') as inFile:
                    data=csv.reader(inFile)

                    #outFile = open('2.csv','w')
                    listLine = [['Name', ' Address', ' Phone']]
                    addata="Null"
                    count=0
                    for line in data:
                              x1=""



                              if line:
                                        listLine.append(line)
                                        #print line
                    for data in listLine:
                              admin=""

                              if data:
                                        ls=[]

                                        count+=1
                                        if count==5:
                                                  data[0]='Division'
                                                  data[1]='Name'
                                                  data.insert(2,'Department')
                                                  data.insert(3,'PhonoNo')
                                                  data.insert(4,'Email')
                                                  print data
                                                  with open(TownshipName,'ab') as f:
                                                                                writer=csv.writer(f)
                                                                                writer.writerow(data)


                                        x=re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',str(data))
                                        if x:

                                                  x1=x.group()
                                                  if len(data)==1 and x1 is not None:


                                                            #ls=[]
                                                            ls=listLine[count-2]
                                                            l=len(ls)+1
                                                            #print ls
                                                            ls.insert(len(ls)+1,x1)
                                                            #print ls
                                                           #



                                        if len(data)==1:
                                                  x=re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',str(data))
                                                  if not x and data[0] not in findlist:

                                                            addata=data
                                                            #print addata
                                                  ls.insert(0,addata)
                                                  if len(ls)>1:
                                                            indices='[',']'
                                                            line1=[]
                                                            for r in ls:
                                                                      sss=str(r)
                                                                      try:

                                                                                sss=sss.strip('[')
                                                                                sss=sss.strip('.')
                                                                                sss=sss.strip(']')
                                                                                sss=sss.strip(',')
                                                                                sss=sss.strip('\'')
                                                                                sss=sss.strip('\"')
                                                                                sss=sss.strip()
                                                                                sss=sss.strip('\"')
                                                                                sss=sss.strip("\'")
                                                                                sss=sss.replace(" ","")
                                                                                #print sss
                                                                                #sss= sss[1:-1]
                                                                                #sss=sss.strip('"')
                                                                                #sss= sss[1:]
                                                                                line1.append(sss)
                                                                      except:
                                                                                pass
                                                            #print line1
                                                            SplitName(line1)










ToRemoveDuplicateValues()