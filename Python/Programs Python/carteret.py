import urllib2
from bs4 import BeautifulSoup

url="http://www.carteret.net/content/2865/default.aspx"
town=url.split('.')[1]
print town
opener=urllib2.build_opener()
print "Builded opener"
opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
print "added headers"
response=opener.open(url)
print "Took Response"
#Storing the Browser data to  variable
soup=BeautifulSoup(response)
#class="ContentTemp_Zebra"
datasets=[]
table=soup.find('table',{'class':'ContentTemp_Zebra'})
if table:
          for row in table.find_all("tr"):
                    dataset = row.get_text()#.encode('utf-8')
                                        #print dataset
                    datasets.append(dataset)
          print datasets

          for p in datasets:
                                        #count+=1
                                        #print count
                                        p=p.encode('ascii','ignore')
                                        p=str(p)
                                        p=p.splitlines()
                                        p=filter(None,p)
                                        p=list(p)
                                        ls=[]
                                        ls.insert(0,town)
                                        for st in p:
                                                  st1=st.strip('\t')
                                                  ls.append(st1)
                                        if len(ls)==2:
                                                  pass
                                        else:

                                                  st=str(ls)
                                                  st1=st.strip('[')
                                                  st2=st1.strip(']')
                                                  st3=st2.strip("'")
                                                  st4=str(st3.replace("'", ""))
                                                  #st4=st4.remove(' Email')
                                                  st5=" ".join(st4.split())

                                                  file=open(town+".csv",'a')
                                                  file.write(st5)
                                                  file.write("\n")
                                                  file.close()

                                                  print st5

