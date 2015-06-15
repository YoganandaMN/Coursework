#6 a
x<-sample(0:999,250,replace = T)
y<-sample(0:999,250,replace = T)

a<-c()
b<-c()
for (i in 2:250){
          #print((sin(y[1]))/(cos(x[2])))
          a<-c(a,y[i]-x[i-1])
#6 b          
          b<-c(b,(sin(y[i-1]))/(cos(x[i])))
}
a
b
#6 c
cc<-c()
for (i in 3:250){
          cc<-c(cc,(x[i-2]+x[i-1]-x[i]))
          #cc<-c(cc,(x[i-2]+x[i-1]-x[i]))          
}
cc
