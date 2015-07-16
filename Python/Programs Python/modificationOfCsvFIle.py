import csv
import sys
import string
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename


def main():
          delete_list = ['COUNCIL ','Council Standing ','COUNCIL','Mayor']
          Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
          filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
          file=filename.split('/')[-1]
          #file="BoroughOfSouthRiver.csv"
          filancsv=file.split('.')
          name=filancsv[0]+"final"+".csv"
          name1=filancsv[0]+"fCouncil"+".csv"
          print name1,name
          path = r"E:\Python Programs\New folder\FinalCSV"
          if not os.path.exists(path):
                    print os.makedirs(path)
                    print "created"

          with open(file) as f:
                    handler=csv.reader(f)
                    for data in handler:

                              try:
                                        data1=[]
                                        data1=data
                                        if data1[0] in idelete_list:
                                                  print data1
                                                  '''
                                                  try:
                                                            with open(os.path.join(path,name1), 'a') as file:
                                                                      file.write(str(data1)+"\n")
                                                                      print data1
                                                                      print name1+" "+"File is created"

                                                  except IOError as (errno,strerror):
                                                            print "I/O error({0}): {1}".format(errno, strerror)
                                                  '''

                                        else:
                                                  #print data1

                                                  '''
                                                  try:
                                                            with open(os.path.join(path,name), 'a') as file1:
                                                                      file1.write(str(data1)+"\n")
                                                                      print name+" "+"File is created"

                                                  except IOError as (errno,strerror):
                                                            print "I/O error({0}): {1}".format(errno, strerror)
                                                  '''

                              except:
                                        pass
if __name__ == '__main__':
    main()
