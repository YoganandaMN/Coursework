import urllib2
from bs4 import BeautifulSoup
def main():
          datasets = []
          def Contact_Info():
                    url=raw_input('enter the iinput')
                    #url="http://www.southrivernj.org/elected_officials.html"
                    opener=urllib2.build_opener()
                    print "Builded opener"
                    opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
                    print "added headers"
                    response=opener.open(url)
                    print "Took Response"
                    soup=BeautifulSoup(response)
                    CranburyTownship=soup.find('table',{'border':'1','bordercolor':'#000000'})
                    if CranburyTownship:
                              print "CranburyTownship mayor and council"
                              #print table.get_text()
                              FetchThe_Data(table)

                    NorthBrunswick=soup.find('table',{'width':'775','border':'1','align':'center','cellpadding':'5','cellspacing':'1'})
                    if NorthBrunswick:
                              print "NorthBrunswick"
                              print "Contacts"
                              print table.get_text()
                              FetchThe_Data(NorthBrunswick)

                    NorthBrunswick1=soup.find('table',{'width':'80%','border':'0','align':'center','cellpadding':'6','cellspacing':'0'})
                    if NorthBrunswick1:
                              print "NorthBrunswick"
                              print "councilMembers"
                              FetchThe_Data(NorthBrunswick1)
                              print table1.get_text()

                    BoroughOfSouthRiver=soup.find('table',{'bordercolor':'#660033','bgcolor':'#F3F3F3'})
                    if BoroughOfSouthRiver:
                              print "BoroughOfSouthRiver"
                              FetchThe_Data(BoroughOfSouthRiver)

                    BoroughOfSpotswood=soup.find('table',{'bordercolorlight':'#000000','bgcolor':'#FFFFFF','bordercolordark':'#000000'})
                    if BoroughOfSpotswood:
                              print "BoroughOfSpotswood"
                              FetchThe_Data(BoroughOfSpotswood)

                    BoroughOfMiddlesex=soup.find('table',{'style':'border: 1px solid #000000; width: 700px;'})
                    if BoroughOfMiddlesex:
                              print "BoroughOfMiddlesex"
                              FetchThe_Data(BoroughOfMiddlesex)

                    TownshipOfOldBridge=soup.find('div',{'id':'wide','class':'grid_8 alpha omega'})
                    if TownshipOfOldBridge:
                    #print soup.find('h1', {'class': 'utility clearfix'})

                    #print table.get_text('h1')
                              print "TownshipOfOldBridge"
                              FetchThe_Data(TownshipOfOldBridge)

                    MonroeTownship=soup.find('div',{'id':'printReady'})
                    if MonroeTownship:
                              print "MonroeTownship Contacts"
                              FetchThe_Data(MonroeTownship)

                    CityOfNewBrunswick=soup.find('section',{'class':'entry'})
                    if CityOfNewBrunswick:
                              print "CityOfNewBrunswick"
                              FetchThe_Data(CityOfNewBrunswick)

                    TownshipOfPiscataway=soup.find('table',{'style':'width: 650px; border-collapse: collapse; font-family: verdana, arial, helvetica, sans-serif; color: rgb(0,0,0)'})
                    if TownshipOfPiscataway:
                              print "TownshipOfPiscataway"
                              FetchThe_Data(TownshipOfPiscataway)
                    TownshipOfPiscataway1=soup.find('table',{'style':'width: 100%;','cellpadding':'5'})
                    if TownshipOfPiscataway1:
                              print "TownshipOfPiscataway Council"
                              FetchThe_Data(TownshipOfPiscataway1)

                    TownshipOfPlainsboro=soup.find('div',{'class':'inner-content-box with-widgets'})
                    if TownshipOfPlainsboro:
                              print "TownshipOfPlainsboro"
                              FetchThe_Data(TownshipOfPlainsboro)

                    SouthBrunswickTownship=soup.find('table',{'style':'width: 75%;','border':'1','cellpadding':'2'})
                    if SouthBrunswickTownship:
                              print "SouthBrunswickTownship"
                              FetchThe_Data(SouthBrunswickTownship)

                    BoroughOfHelmetta=soup.find('table',{'width':'100%','border':'0','cellpadding':'0','cellspacing':'3'})
                    if BoroughOfHelmetta:
                              print "BoroughOfHelmetta"
                              FetchThe_Data(BoroughOfHelmetta)

                    BoroughOfHighlandPark=soup.find('table',{'summary':'Employee Info'})
                    if BoroughOfHighlandPark:
                              print "BoroughOfHighlandPark Contact"
                              FetchThe_Data(BoroughOfHighlandPark)
                    BoroughOfHighlandPark1=soup.find('table',{'summary':'City Directory'})
                    if BoroughOfHighlandPark1:
                              print "BoroughOfHighlandPark Council"
                              FetchThe_Data(BoroughOfHighlandPark1)





          def Mayor_Council():

                    print "Mayor_Council Block"
                    url="http://www.southrivernj.org/elected_officials.html"
                    opener=urllib2.build_opener()
                    print "Builded opener"
                    opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
                    print "added headers"
                    response=opener.open(url)
                    print "Took Response"
                    soup=BeautifulSoup(response)
                    table=soup.find("table",attrs={'cellpadding':'5','bordercolor':'#660033'})
                    FetchThe_Data(table)
                    #print table.getText()cellpadding="5"

          def FetchThe_Data(table):
                    for row in table.find_all("tr"):
                              dataset = row.get_text().encode('utf-8')
                              datasets.append(dataset)
                    ToGetItIn_manner(datasets)


          def ToGetItIn_manner(datasets):
                    for data in datasets:
                              p=str(data)
                              p=p.splitlines()
                              p=filter(None,p)
                              st=str(p)
                              #st=st.strip('\t')
                              st1=st.strip('[')
                              st2=st1.strip(']')
                              st3=st2.strip("'")
                              st4=str(st3.replace("'", ""))
                              print " ".join(st4.split())
                              #print st5.strip('\t')




          Contact_Info()
          #Mayor_Council()


if __name__ == '__main__':
    main()

