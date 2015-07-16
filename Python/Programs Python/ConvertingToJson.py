import csv
import sys
import json
from itertools import islice
from Tkinter import Tk
from tkFileDialog import askopenfilename
import FirstClass
import FirstClassDept
def main():
          fieldnames=('Department','Name','Phone','Email','Address','fax')
          delete_list = ['COUNCIL ','Council Standing ','COUNCIL','Mayor',' Councilman ',' Council Woman ',' Council President ','MayorMarlene ','Councilman','Council President',' Councilwoman ',' Mayor ','Councilwoman ','Council President ','Councilman ','Councilman Donald Applegate','Councilman Thomas Reilly','Council President Michael Gross','Councilman Christine Noble','Councilman Zusette Dato','Mayor: Fred Henry','Mayors Secretary: Stacey Kenndy',' Council President',' Council Vice President',' Councilman',' Councilman',' Councilwoman','Councilwoman','Deputy Mayor',' President',' Vice President',' Mayor','Finance DepartmentGregory Mayers']
          print (fieldnames)
          filename='BoroughOfSouthRiver.csv'
          Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
          filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
          file=filename.split('/')[-1]
          name=file.split('.')
          TownshipName=name[0]
          print TownshipName
          print file
          with open(file) as f:
                    handler=csv.reader(f)
                    for data in handler:

                              try:
                                        data1=[]
                                        data1=data
                                        if data1[0] in delete_list:
                                                  #print data1[0]
                                                  #print data1
                                                  #FirstClass.filterData(TownshipName,data1)
                                                  pass
                                        elif data1[1] in delete_list:
                                                  #print data1
                                                  #FirstClass.filterData(TownshipName,data1)
                                                  pass

                                        else:
                                                  print len(data1)
                                                  print data1

                                                  #FirstClassDept.filterData(TownshipName,data1)

                              except:
                                        pass
if __name__ == '__main__':
    main()
