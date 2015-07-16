import csv
import string
from Tkinter import Tk
from tkFileDialog import askopenfilename
import re
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
print name
TownshipName="New"+name[0]+".csv"
print TownshipName
Heading=['TownshipName','Division','Name','Department','PhoneNumber','Ext']
def modify():
          with open(file,'r') as f:
                    reader=csv.reader(f)
                    print Heading
                    with open(TownshipName,'ab') as f:
                              writer=csv.writer(f)
                              writer.writerow(Heading)
                    count=0
                    for line in reader:

                              if line:
                                        count+=1

                                        try:
                                                  line[-1]
                                                  line[-1]= line[-1].replace("email","")
                                                  line[-1]=line[-1].strip()

                                                  if line[-1].startswith("ext"):
                                                            #print line
                                                            l=line[-1].split('-')
                                                            line[-1]=l[0]

                                                  #print line
                                        except:pass
                                        if count==1:
                                                  try:
                                                            PNo=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',str(line))
                                                            PhoneNo=PNo.group()
                                                            #print PhoneNo
                                                  except:
                                                            pass
                                        else:


                                                  PNo=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',str(line))
                                                  if PNo:
                                                            PhoneNo=PNo.group()
                                                            try:
                                                                      if len(line)==2:
                                                                                r=re.split('(\D+)', str(line[1]))
                                                                                #print r
                                                                                #r1=line[0]
                                                                                r2=r[2]+r[3]+r[4]+r[5]+r[6]
                                                                                #print r2
                                                                                #line[0]=r1
                                                                                line[1]=r2
                                                                                #To split the string when it encounters the Capital letters
                                                                                rr=re.findall('[A-Z][^A-Z]*', line[0])
                                                                                #print rr
                                                                                r1=rr[0]+rr[1]
                                                                                r2=rr[2]+rr[3]
                                                                                #print r2
                                                                                line[0]=r1
                                                                                line.insert(1,r2)
                                                                                line.insert(0,TownName)
                                                                                with open(TownshipName,'ab') as f:
                                                                                                    writer=csv.writer(f)
                                                                                                    writer.writerow(line)
                                                                                print line

                                                                      r=re.split('(\D+)', str(line[0]))
                                                                      #print r
                                                                      r2=r[2]+r[3]+r[4]+r[5]+r[6]
                                                                      line[0]=r[1]
                                                                      line.insert(1,r2)
                                                                      line.insert(0,TownName)
                                                                      print line
                                                                      #print r

                                                            except:
                                                                      pass
                                                            #print line
                                                  else:
                                                            #this is for Council Members
                                                            if len(line)==1:
                                                                      line1=str(line[0])
                                                                      line1=line1.split(" ")
                                                                      if len(line1)==2:
                                                                                line1.insert(0,TownName)
                                                                                with open(TownshipName,'ab') as f:
                                                                                                    writer=csv.writer(f)
                                                                                                    writer.writerow(line1)
                                                                                print line1
                                                                                #print line
                                                                                pass
                                                                      elif len(line1)==3:
                                                                                r1=line1[0]
                                                                                r2=line1[1]+line1[2]
                                                                                line[0]=r1
                                                                                line.insert(1,r2)
                                                                                line.insert(0,TownName)
                                                                                with open(TownshipName,'ab') as f:
                                                                                                    writer=csv.writer(f)
                                                                                                    writer.writerow(line)
                                                                                print line
                                                                      elif len(line1)==5:
                                                                                r1=line1[0]+line1[1]
                                                                                r2=line1[2]+line1[3]+line1[4]
                                                                                line[0]=r1
                                                                                line.insert(1,r2)
                                                                                line.insert(0,TownName)
                                                                                with open(TownshipName,'ab') as f:
                                                                                                    writer=csv.writer(f)
                                                                                                    writer.writerow(line)
                                                                                print line
                                                                      elif len(line1)>5:
                                                                                #print line1
                                                                                r1=line1[0]+line1[1]+line1[2]+line1[3]
                                                                                r2=line1[4]+line1[5]
                                                                                line[0]=r1
                                                                                line.insert(1,r2)
                                                                                line.append(PhoneNo)
                                                                                line.insert(0,TownName)
                                                                                line[-1],line[-2]=line[-2],line[-1]
                                                                                with open(TownshipName,'ab') as f:
                                                                                                    writer=csv.writer(f)
                                                                                                    writer.writerow(line)
                                                                                print line
                                                            else:
                                                                      #print line[0]
                                                                      count1=0
                                                                      rr=re.findall('[A-Z][^A-Z]*', line[0])
                                                                      if len(rr)==4:
                                                                                r1=rr[0]+rr[1]
                                                                                r2=rr[2]+rr[3]
                                                                                line[0]=r1
                                                                                line.insert(1,r2)
                                                                                line.append(PhoneNo)
                                                                                line[-1],line[-2]=line[-2],line[-1]
                                                                                line.insert(0,TownName)
                                                                                with open(TownshipName,'ab') as f:
                                                                                                    writer=csv.writer(f)
                                                                                                    writer.writerow(line)
                                                                                print line

                                                                      elif len(rr)==5:
                                                                                count1+=1
                                                                                #print line[0]
                                                                                if count<20 or count==21:
                                                                                          r1=rr[0]+rr[1]+rr[2]
                                                                                          r2=rr[3]+rr[4]
                                                                                          line[0]=r1
                                                                                          line.insert(1,r2)
                                                                                          line.append(PhoneNo)
                                                                                          line[-1],line[-2]=line[-2],line[-1]
                                                                                          #print line
                                                                                else:
                                                                                          r1=rr[0]+rr[1]
                                                                                          r2=rr[2]+rr[3]+rr[4]
                                                                                          line[0]=r1
                                                                                          line.insert(1,r2)
                                                                                          line.append(PhoneNo)
                                                                                          line[-1],line[-2]=line[-2],line[-1]
                                                                                          #print line
                                                                                if count==16:
                                                                                          pass
                                                                                          '''
                                                                                          s=str(line)
                                                                                          aa1=(s.partition('Ron Yake')[0])
                                                                                          aa2=(s.partition('Ron Yake')[1])
                                                                                          aa3=(s.partition('Ron Yake')[2])
                                                                                          #aa1.append(PhoneNo)
                                                                                          print aa1
                                                                                          aa=aa2,aa3
                                                                                          #aa.append(PhoneNo)
                                                                                          print aa
                                                                                          '''
                                                                                else:
                                                                                          #line.append(PhoneNo)
                                                                                          #line[-1],line[-2]=line[-2],line[-1]
                                                                                          pass
                                                                                          line.insert(0,TownName)
                                                                                          with open(TownshipName,'ab') as f:
                                                                                                    writer=csv.writer(f)
                                                                                                    writer.writerow(line)
                                                                                          print line
                                                                      else:
                                                                                ll=str(line[0])
                                                                                if ll.startswith('Police'):
                                                                                          rr=re.findall('[A-Z][^A-Z]*', ll)
                                                                                          #print rr
                                                                                          r1=rr[0]+rr[1]+rr[2]+rr[3]
                                                                                          r2=rr[4]+rr[5]
                                                                                          line[0]=r1
                                                                                          line.insert(1,r2)
                                                                                          line.append(PhoneNo)
                                                                                          line[-1],line[-2]=line[-2],line[-1]
                                                                                          line.insert(0,TownName)
                                                                                          with open(TownshipName,'ab') as f:
                                                                                                    writer=csv.writer(f)
                                                                                                    writer.writerow(line)
                                                                                          print line




modify()
