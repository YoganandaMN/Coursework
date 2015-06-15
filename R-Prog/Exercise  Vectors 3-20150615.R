#3.a
v<-c()
a<-0.1^seq(3,36,3)
b<-0.2^seq(1,34,3)
for (i in 1:12)
{
          
          v<-c(v,a[i],b[i])
          #v<-c()    
}
v

#3.b
a<-c()
for (i in 1:25){
          
          a<-c(a,((2^i) /i))    
}
a

#OR
y<-c(2^(1:25)/(1:25))
y
