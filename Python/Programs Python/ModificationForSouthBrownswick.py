import csv
import re
from Tkinter import Tk
from tkFileDialog import askopenfilename
#SouthBrunswickTownship.csv
Tk().withdraw()
ReadFile="CranburyTownship.csv"
t='South Brunswick Township'
filename=askopenfilename()
print filename
file=str(filename.split('/')[-1])
print file
name=file.split('.')
TownshipName="New"+name[0]+".csv"
print TownshipName
memberslist=['Joseph J. Camarota Jr (Councilman)','Charlie Carley (Councilman)','Josephine "Jo" Hochman','Chris Killmurray (Deputy Mayor)','Frank Gambatese (Mayor)']
striplist='[',']',')'

with open (file,'r') as inFile:
                    handler=csv.reader(inFile)
                    count=0
                    #pno='None'
                    for line in handler:

                              if line:
                                        count+=1
                                        print count
                                        if count==1 or count==2:
                                                  if count==1:
                                                            print line
                                                            PhoneNo=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',str(line))
                                                            Pno=PhoneNo.group()
                                                            #print Pno
                                                  else:
                                                            line.insert(2,'PhoneNUmber')
                                                            line.insert(0,'TownshipName')
                                                            with open(TownshipName,'ab') as f:
                                                                                writer=csv.writer(f)
                                                                                writer.writerow(line)

                                                            #print name
                                                            print line
                                        else:
                                                  #print line
                                                  if line[0] in memberslist:
                                                            if count is not 46:
                                                                      line1=str(line)
                                                                      line2=line1.split('(')
                                                                      name= [re.sub('[\]\[\(\)\']', '', name)for name in line2]
                                                                      #print name
                                                                      '''
                                                                      with open("test.csv",'ab') as f:
                                                                                writer=csv.writer(f)
                                                                                writer.writerow(name)
                                                                      '''

                                                                      #print name



                                                                      pass
                                                  else:
                                                            phone=re.search('\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}',str(line))
                                                            if phone:
                                                                      line.insert(0,t)

                                                                      #print phone.group()
                                                                      with open(TownshipName,'ab') as f:
                                                                                          writer=csv.writer(f)
                                                                                          writer.writerow(line)

                                                                      print line
                                                            else:
                                                                      try:
                                                                                line.append(Pno)
                                                                                line[-2],line[-1]=line[-1],line[-2]
                                                                                line.insert(0,t)
                                                                                #print line
                                                                                with open(TownshipName,'ab') as f:
                                                                                          writer=csv.writer(f)
                                                                                          writer.writerow(line)

                                                                                print line
                                                                      except:
                                                                                pass

                                                            #pass


