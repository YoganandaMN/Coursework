
import urllib2 # For Reading the Web Page
import xlrd # For Manipulation and reading Excel Sheets

def main():
    def read(url2,company):
        #Parsing the Browser data
        try:
                opener=urllib2.build_opener()
                opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
                #request=urllib2.Request(url2) #Requesting the Url
                handle=opener.open(url2)
                #handle=urllib2.urlopen(url2) #opens the url
        except:
                Error="Url opening or reading Error"
                write=str(Error+"\n"+company+"\t"+url2)
                op=open(company+".txt",'wb')
                op.write(Error)
                print Error
                print url2,"Has been Written to file",company


        else:
                html=handle.read()  #Reads the data in the browser
                op=open(company+".txt",'wb') #Creates File As a Company name
                p=op.write(html)    #Writes the browser data into a file
                print ("\n")
                #print p
                op.close()  #closes the file
                print url2,"Has been Written to file",company
                #print company
                #print url






    #Location of the excel file
    locatiion="C:\Users\Durga\OneDrive\Documents/county_township_information.xlsx"
    workbook=xlrd.open_workbook(locatiion) #loading The Excel sheet
    sheet=workbook.sheet_by_index(0)
    rno=sheet.nrows
    print sheet.ncols
    url=""  #initializing url
    company=""  #initializing companey

    for row in range(2,sheet.nrows):
        print("\n")
        for col in range(sheet.ncols):
            data=str(sheet.cell_value(row,col)) #Reading the Excel data by Using Cell Index
            #print data

#Checks whether url is present IF not Assigns Companey And url to null and break the statement
            if data=="":
                print "url not found for",company
                url=""
                company=""
                break

#Checks whether the data is URL

            elif data.startswith("www"):

                url=data
                url2="http://"+url
                read(url2,company);

#IF the data is not an URL and NULL it will take it as a company name
            else:
                company=data

if __name__ == '__main__':
    main()
