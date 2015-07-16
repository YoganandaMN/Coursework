import csv
from Tkinter import Tk
from tkFileDialog import askopenfilename
import re
Tk().withdraw()
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
                    count=0
                    print Heading

                    with open(TownshipName,'ab') as f:
                              writer=csv.writer(f)
                              writer.writerow(Heading)

                    linstline=[' President',' Vice President',' Vice President']
                    for line in reader:
                              if line:
                                        count+=1
                                        if count==1:
                                                  PNo=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',str(line))
                                                  PhoneNo=PNo.group()
                                                  print PhoneNo
                                        elif count>2:

                                                  if len(line)==1:
                                                            line1=str(line)
                                                            data=line1.strip('[')
                                                            data=data.strip(']')
                                                            data=data.strip('\'')


                                                            #print data
                                                  else:
                                                            #pass
                                                            if line[-1] in linstline:


                                                                      line.insert(0,TownName)
                                                                      line.insert(1,'NA')
                                                                      with open(TownshipName,'ab') as f:
                                                                                writer=csv.writer(f)
                                                                                writer.writerow(line)

                                                                      print line
                                                            else:


                                                                      line.insert(0,data)
                                                                      line.append(PhoneNo)
                                                                      line[-1],line[-2]=line[-2],line[-1]
                                                                      line.insert(0,TownName)
                                                                      with open(TownshipName,'ab') as f:
                                                                                writer=csv.writer(f)
                                                                                writer.writerow(line)

                                                                      #pass
                                                                      print line


modify()