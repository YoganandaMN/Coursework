import csv
import string
from Tkinter import Tk
from tkFileDialog import askopenfilename
def ToRemoveDuplicateValues():
          Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
          filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
          file=filename.split('/')[-1]
          print file
          name=file.split('.')
          TownshipName="New"+name[0]+".csv"

          #inFile = open(file,'r')


          with open (file,'r') as inFile:
                    data=csv.reader(inFile)

                    #outFile = open('2.csv','w')
                    listLine = [['Name', ' Address', ' Phone']]
                    addata="Null"
                    count=0
                    for line in data:

                              if line:
                                        count+=1
                                        #print count
                                        if count==3:
                                                  line.insert(0,"Division")
                                                  line.insert(2,"Department")
                                                  with open(TownshipName,'ab') as f:
                                                            writer=csv.writer(f)
                                                            writer.writerow(line)
                                                  print line
                                                  listLine.append(line)
                                                  #print listLine
                              if len(line)==1 and line not in listLine:
                                        listLine.append(line)
                                        addata=str(line)
                                        try:
                                                  addata=addata.strip('[')
                                                  addata=addata.strip(']')
                                                  addata=addata[1:-1]
                                                  #addata=addata.strip('"')
                                                  #print addata
                                        except:
                                                  pass


                                        #print addata


                              if line in listLine:
                                        continue

                              elif len(line) > 1:
                                        line.insert(0,addata)
                                        with open(TownshipName,'ab') as f:
                                                            writer=csv.writer(f)
                                                            writer.writerow(line)
                                        print line

ToRemoveDuplicateValues()