import urllib2
from bs4 import BeautifulSoup
import time
import xlrd
import re
import string
def main():



          #url=raw_input('enter the url')
          def Identifing_The_Data(soup,url):
                    datasets = []
                    BoroughOfSayreville=soup.find('table',{'width':'100%','border':'0','cellpadding':'0','cellspacing':'3'})
                    if BoroughOfSayreville and url=="http://www.sayreville.com/Cit-e-Access/ContactInfo/?TID=87&TPID=8641":
                              print "BoroughOfSayreville"
                              for row in BoroughOfSayreville.find_all("tr"):
                                        dataset = row.get_text()#.encode('utf-8')
                                        datasets.append(dataset)
                              ToGetItIn_manner(datasets,"BoroughOfSayreville",url)

                    CranburyTownship=soup.find('table',{'border':'1','bordercolor':'#000000'})
                    if CranburyTownship:
                              print "CranburyTownship mayor and council"
                              #print table.get_text()
                              FetchThe_Data(CranburyTownship,"CranburyTownship",datasets,url)
                              exit


                    BoroughOfSouthRiver=soup.find('table',{'bordercolor':'#660033','bgcolor':'#F3F3F3'})
                    if BoroughOfSouthRiver:
                              print "BoroughOfSouthRiver"
                              FetchThe_Data(BoroughOfSouthRiver,"BoroughOfSouthRiver",datasets,url)

                    BoroughOfSpotswood=soup.find('table',{'bordercolorlight':'#000000','bgcolor':'#FFFFFF','bordercolordark':'#000000'})
                    if BoroughOfSpotswood:
                              print "BoroughOfSpotswood"
                              FetchThe_Data(BoroughOfSpotswood,"BoroughOfSpotswood",datasets,url)

                    BoroughOfMiddlesex=soup.find('table',{'style':'border: 1px solid #000000; width: 700px;'})
                    if BoroughOfMiddlesex:
                              print "BoroughOfMiddlesex"
                              FetchThe_Data(BoroughOfMiddlesex,"BoroughOfMiddlesex",datasets,url)

                    MonroeTownship=soup.find('div',{'id':'printReady'})
                    if url=="http://www.monroetwp.com/township_council.cfm":
                            FetchThe_Data1(MonroeTownship,"MonroeTownship Contacts",datasets,url)
                    elif MonroeTownship:
                              print "MonroeTownship Contacts"
                              FetchThe_Data(MonroeTownship,"MonroeTownship Contacts",datasets,url)



                    TownshipOfPlainsboro=soup.find('div',{'class':'inner-content-box with-widgets'})
                    if url=="http://www.plainsboronj.com/content/mayor-township-committee":
                              FetchThe_Data_TownshipOfPlainsboro(TownshipOfPlainsboro,"TownshipOfPlainsboro",datasets,url)
                    elif TownshipOfPlainsboro:
                              print "TownshipOfPlainsboro"
                              FetchThe_Data(TownshipOfPlainsboro,"TownshipOfPlainsboro",datasets,url)


                    BoroughOfHelmetta=soup.find('table',{'width':'100%','border':'0','cellpadding':'0','cellspacing':'3'})
                    if url=="http://www.helmettaboro.com/Cit-e-Access/ContactInfo/?TID=102&TPID=10562" and BoroughOfHelmetta:
                              print "BoroughOfHelmetta"
                              FetchThe_Data(BoroughOfHelmetta,"BoroughOfHelmetta",datasets,url)

                              #FetchThe_Data(BoroughOfHelmetta,"BoroughOfSayreville",datasets)


                    CityOfSouthAmboy=soup.find('div',{'class':'field-item even','property':'content:encoded'})
                    if CityOfSouthAmboy:
                              print "CityOfSouthAmboy"
                              #print CityOfSouthAmboy.get_text()
                              FetchThe_Data(CityOfSouthAmboy,"CityOfSouthAmboy",datasets,url)

                    SouthBrunswickTownship=soup.find('div',{'class':'body sec_summary'})
                    if url=="http://www.sbtnj.net/index.asp?Type=B_LIST&SEC={46A301B7-6D94-4CC3-8C82-EE4A17443CA2}" and SouthBrunswickTownship:
                              dataset=SouthBrunswickTownship.find('p').get_text()#.encode('utf-8')
                              datasets.append(dataset)
                              print "SouthBrunswickTownship"
                              #print CityOfSouthAmboy.get_text()
                              FetchThe_Data(SouthBrunswickTownship,"SouthBrunswickTownship",datasets,url)
                              #class="contentbox_center_body"
                    SouthBrunswickTownship_Council=soup.find('div',{'class':'contentbox_center_body'})
                    if SouthBrunswickTownship_Council:
                              print "SouthBrunswickTownship_Council"
                              #print SouthBrunswickTownship_Council.get_text()
                              FetchThe_Data_SouthBrunswickTownship_Council(SouthBrunswickTownship_Council,"SouthBrunswickTownship",datasets,url)

                    TownshipOfEdison=soup.find('div',{'class':'post'})
                    if url=="http://www.edisonnj.org/contact_us/index.php" and TownshipOfEdison:

                              print " TownshipOfEdison"
                              print datasets.append(TownshipOfEdison.find('strong').get_text())
                              table=TownshipOfEdison.find('table',{'border':'1','align':'center'})
                              FetchThe_Data(table,"TownshipOfEdison",datasets,url)

                    TownshipOfEdison1=soup.find('div',{'class':'post'})
                    if url=="http://www.edisonnj.org/town_hall/council/council_members.php" and TownshipOfEdison1:
                              print "TownshipOfEdison1"
                              name="TownshipOfEdison"
                              for div in TownshipOfEdison1.findAll('div'):
                                        dataset=div.get_text()
                                        datasets.append(dataset)
                              ToGetItIn_manner(datasets,name,url)

                    BoroughOfJamesburg1=soup.find("div",{'id':'main'})
                    if BoroughOfJamesburg1:
                              print "BoroughOfJamesburg1:"
                              for row in BoroughOfJamesburg1.find_all('p'):
                                        dataset = row.get_text(strip=True)#.encode('utf-8')
                                        datasets.append(dataset)
                              ToGetItIn_manner(datasets,"BoroughOfJamesburg",url)



          def Contact_Info(url):
                    #fetching the Link
                    opener=urllib2.build_opener()
                    print "Builded opener"
                    opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
                    print "added headers"
                    response=opener.open(url)
                    print "Took Response"
                    #Storing the Browser data to  variable
                    soup=BeautifulSoup(response)
                    Identifing_The_Data(soup,url)



          def FetchThe_Data_SouthBrunswickTownship_Council(table,name,datasets,url):
                    print "Came inside FetchThe_Data_SouthBrunswickTownship_Council"
                    for row in table.find_all('div',{'class':'itemSummaryTitle'}):
                              dataset = row.get_text()#.encode('utf-8')
                              datasets.append(dataset)
                    #print datasets
                    ToGetItIn_manner(datasets,name,url)



          def FetchThe_Data(table,name,datasets,url):
                    #time.sleep(3)
                    print "Came inside FetchThe_Data"
                    if url=="http://plainsboronj.com/content/departmental-directory":
                              dataset=table.find('p').getText()#.encode('utf-8')
                              datasets.append(dataset)
                    for row in table.find_all("tr"):
                              dataset = row.get_text()#.encode('utf-8')
                              datasets.append(dataset)
                    #print datasets
                    ToGetItIn_manner(datasets,name,url)



          def FetchThe_Data1(table,name,datasets,url):
                    print "Came inside FetchThe_Data1"

                    for row in table.find_all("h4"):
                              dataset = row.get_text()#.encode('utf-8')
                              datasets.append(dataset)
                    #print datasets
                    ToGetItIn_manner(datasets,name,url)



          def FetchThe_Data_TownshipOfPlainsboro(table,name,datasets,url):
                    print "Came inside FetchThe_Data_TownshipOfPlainsboro"
                    dataset=table.find('h2').getText()#.encode('utf-8')

                    for row in table.find_all("strong"):
                              dataset = row.get_text()#.encode('utf-8')
                              datasets.append(dataset)
                    ##print datasets
                    ToGetItIn_manner(datasets,name,url)




          def ToGetItIn_manner(datasets,name,url):
                    print "Data Cleaning"
                    for p in datasets:
                              p=p.encode('ascii','ignore')
                              p=str(p)
                              p=p.splitlines()
                              p=filter(None,p)
                              p=list(p)
                              ls=[]
                              for st in p:
                                        st1=st.strip('\t')
                                        ls.append(st1)

                              st=str(ls)
                              st1=st.strip('[')
                              st2=st1.strip(']')
                              st3=st2.strip("'")
                              st4=str(st3.replace("'", ""))
                              st5=" ".join(st4.split())

                              print st5
                              '''
                              # Writing to a file
                              file=open(name+".csv",'a')
                              file.write(st5+"\n")

                    if(file != " "):
                              file.write("\n"+"\n"+"\n")
                    print name+" "+"File is created"
                    file.close()
                    '''

                              #print st5.strip('\t')




          #Contact_Info(url)


          #taking Input From th Xl Sheet
          location="TownshipInput.xls"
          workbook=xlrd.open_workbook(location)
          sheet=workbook.sheet_by_index(0)
          for row in range(1,sheet.nrows):
                    print("\n")
                    for col in range(3,sheet.ncols):
                              data=str(sheet.cell_value(row,col))
                              if data=="":
                                        pass
                              else:
                                        url=data
                                        time.sleep(3)
                                        print ("\n")
                                        print url
                                        Contact_Info(url)




          #Fetech_The_Url()


if __name__ == '__main__':
    main()

