import csv
import sys
import json
from itertools import islice
def main():

          fieldnames=('Department','Name','Phone','Email','Address','fax')
          print (fieldnames)
          filename='BoroughOfSouthRiver.csv'

          csv_filename = filename
          print "Opening CSV file: ",csv_filename
          f=open(csv_filename, 'r')
          json_filename = csv_filename.split(".")[0]+".json"
          jsonf = open(json_filename,'w')
          print json_filename
          csvreader = csv.reader(f)

          #header = next(csvreader)
          for row in islice(csvreader , 1, None):
                    if(len(row) is 3):
                              reader = csv.DictReader( f, fieldnames)
                              for data in reader:
                              #print data
                                        json.dump(data, jsonf,ensure_ascii=True)
                    else:
                              print "not 3"
                    #jsonf.write('\n')
          f.close()
          jsonf.close()



if __name__ == '__main__':
    main()
