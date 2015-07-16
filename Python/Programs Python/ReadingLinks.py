#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Durga
#
# Created:     25-06-2015
# Copyright:   (c) Durga 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xlrd
def main():
          location="TownshipInput.xls"
          workbook=xlrd.open_workbook(location)
          sheet=workbook.sheet_by_index(0)
          for row in range(2,sheet.nrows):
                    print("\n")
                    for col in range(3,sheet.ncols):
                              data=str(sheet.cell_value(row,col))
                              if data=="http://www.edisonnj.org/contact_us/index.php":
                                        print "yes"
                              #print data
          print sheet.ncols
          print sheet.nrows
          print sheet
if __name__ == '__main__':
    main()
