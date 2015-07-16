import urllib2
from bs4 import BeautifulSoup
def main():
    #BOROUGH OF JAMESBURG
          def ToGetItIn_manner(datasets):
                    for data in datasets:
                              p=str(data)
                              p=p.splitlines()
                              p=filter(None,p)
                              st=str(p)
                              st1=st.strip('[')
                              st2=st1.strip(']')
                              st3=st2.strip("'")
                              st4=str(st3.replace("'", ""))
                              print " ".join(st4.split())
          datasets=[]
          url=raw_input("enter the url")
          #url="http://www.southrivernj.org/elected_officials.html"
          opener=urllib2.build_opener()
          print "Builded opener"
          opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
          print "added headers"
          response=opener.open(url)
          print "Took Response"
          soup=BeautifulSoup(response)
          BoroughOfJamesburg=soup.findChild("div",{'id':'content'})
          for row in BoroughOfJamesburg.find_all(['p']):
                    if (True):
                    #print row.get_text().encode('utf-8')
                              dataset = row.get_text().encode('utf-8')
                              datasets.append(dataset)
          for row in BoroughOfJamesburg.find_all('div'):
                    dataset = row.get_text().encode('utf-8')
                    datasets.append(dataset)

          #print datasets
          ToGetItIn_manner(datasets)
          #p=soup.findAll("b")
          #print p.getText()
          #for i in p:
           #         print i.gettext()



if __name__ == '__main__':
    main()
