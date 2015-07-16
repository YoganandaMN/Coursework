import csv
import re
from Tkinter import Tk
from tkFileDialog import askopenfilename
Tk().withdraw()
filename=askopenfilename()
file=str(filename.split('/')[-1])
print file
name=file.split('.')
TownshipName="New"+name[0]+".csv"
print TownshipName

with open(file)as f:

          reader=csv.reader(f)
          for lines in reader:
                    ls=[]
                    for items in lines:
                              #print items
                              item1=items[2:-1]
                              if item1.endswith('\''):
                                        itema2=item1[:-1]
                                        ls.append(itema2)
                                        #print itema2
                              elif item1.endswith('\"'):
                                        item11=item1[1:-1]

                                        #pass
                                        #print item1
                                        ls.append(item11)
                              else:
                                        ls.append(item1)

                    with open(TownshipName,'ab') as f:
                              writer=csv.writer(f)
                              writer.writerow(ls)
                    print ls

