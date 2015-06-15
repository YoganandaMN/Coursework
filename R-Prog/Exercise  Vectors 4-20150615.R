#4.a
v<-c()
for (i in c(10:100)){
          t<-(i^3)+(4*(i^2))
          v<-c(v,t)
}
sum(v)

#4.b
f<-c()
for (i in 1:15){
          
          f<-c(f,(((2^i)/i)+((3^i)/i))) 
          
}
sum(f)
