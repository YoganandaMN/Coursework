import urllib2
from bs4 import BeautifulSoup
def main():
          datasets = []
          def Contact_Info():
                    Tem_list=[]
                    '''
                    pr="Contact_Info(): Block"
                    Tem_list=[]
                    Tem_list.append(pr)
                    print Tem_list

                    '''
                    url="http://www.northbrunswicknj.gov/department-locator.html"
                    opener=urllib2.build_opener()
                    print "Builded opener"
                    opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
                    print "added headers"
                    response=opener.open(url)
                    print "Took Response"
                    soup=BeautifulSoup(response)
                    table=soup.find("table",{'border':'1'})
                    #print table.get_text()


                    #headings = [th.get_text() for th in table.find_all("tr").find_all("td")]
                    #print headings

                    for row in table.find_all("tr"):
                              dataset = row.get_text()
                              datasets.append(dataset)
                    ToGetItIn_manner(datasets)

                    #pr=table.getText()
                    #print pr
                    #Tem_list.append(pr)
                    #print Tem_list




          def Mayor_Council():


                    print "Mayor_Council Block"
                    url="http://www.spotswoodboro.com/directory.html"
                    opener=urllib2.build_opener()
                    print "Builded opener"
                    opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
                    print "added headers"
                    response=opener.open(url)
                    print "Took Response"
                    soup=BeautifulSoup(response)
                    table=soup.find("table",{'cellspacing':'0'})
                    print table.getText()

          def ToGetItIn_manner(datasets):
                    for p in datasets:
                              p=p.splitlines()
                              p=filter(None,p)
                              print str(p)




          Contact_Info()
          ToGetItIn_manner(datasets)
          #Mayor_Council()


if __name__ == '__main__':
    main()
