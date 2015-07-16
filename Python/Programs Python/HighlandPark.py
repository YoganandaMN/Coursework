import urllib2
from bs4 import BeautifulSoup
url="http://www.hpboro.com/directory.aspx"
#town=url.split('.')[1]
town='Highland Park'
opener=urllib2.build_opener()
print "Builded opener"
opener.addheaders=[('user_agent','Chrome/41.0.2243.0')]
print "added headers"
response=opener.open(url)
print "Took Response"
#Storing the Browser data to  variable
soup=BeautifulSoup(response)
table=soup.find('table',{'summary':'Employee Info'})#summary="Employee Info"
datasets=[]
d='TownshipName,'+'Department,'+'Telephone'
if table:
          file=open(town+".csv",'a')
          file.write(d)
          file.write("\n")
          file.close()
          count=0
          for row in table.find_all("tr"):
                    dataset = row.get_text()#.encode('utf-8')
                                        #print dataset
                    datasets.append(dataset)
          #print datasets

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
                                        #print st5
                                        sp=st5.split(",")
                                        for data in sp:
                                                  count+=1
                                                  print count
                                                  data1=data.lstrip()
                                                  #print data1
                                                  data2=data1.split("(",1)
                                                  data11= ",(".join(data2)

                                                  data11=town+","+data11
                                                  if count>39:
                                                            pass
                                                  else:
                                                            if count>3:
                                                                      file=open(town+".csv",'a')
                                                                      file.write(data11)
                                                                      file.write("\n")
                                                                      file.close()
                                                                      print data11
