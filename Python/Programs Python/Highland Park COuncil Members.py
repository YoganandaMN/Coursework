import urllib2
from bs4 import BeautifulSoup
url="http://www.hpboro.com/Directory.aspx?DID=32"
#town=url.split('.')[1]
town='Highland Park'
town1='HighlandParkCouncilMembers'
opener=urllib2.build_opener()
print "Builded opener"
opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
print "added headers"
response=opener.open(url)
print "Took Response"
datasets=[]
d='TownshipName,'+'Department,'+'Name'
#Storing the Browser data to  variable
soup=BeautifulSoup(response)
table=soup.find('table',{'summary':'City Directory'})#summary="City Directory"
file=open(town1+".csv",'a')
file.write(d)
file.write("\n")
file.close()
for tag in table.find_all('script'):
    tag.clear()

# Clear every style tag
#for tag in tag.find_all('style'):
#    tag.clear()

# Remove style attributes (if needed)
#for tag in table.find_all(style=True):
#    del tag['style']

for row in table.find_all("tr"):
                    dataset = row.get_text()
                    datasets.append(dataset)

#print datasets
count=0
for p in datasets:

                                        p=p.encode('ascii','ignore')
                                        p=str(p)
                                        p=p.splitlines()
                                        p=filter(None,p)
                                        p=list(p)
                                        ls=[]
                                        #ls.insert(0,town)
                                        for st in p:
                                                  st1=st.strip('\t')
                                                  ls.append(st1)

                                        st=str(ls)
                                        st1=st.strip('[')
                                        st2=st1.strip(']')
                                        st3=st2.strip("'")
                                        st4=str(st3.replace("'", ""))
                                        #st4=st4.remove(' Email')
                                        st5=" ".join(st4.split())
                                        ls1=[]
                                        ls1.append(st5)

                                        for lines in ls1:
                                                  if lines:
                                                            count+=1
                                                            print count
                                                            l=lines.split(',')
                                                            if count>2:
                                                                      r1=l[0]+l[1]
                                                                      r2=l[2]
                                                                      r3=town+","+r2+","+r1
                                                                      file=open(town1+".csv",'a')
                                                                      file.write(r3)
                                                                      file.write("\n")
                                                                      file.close()
                                                                      print r3
