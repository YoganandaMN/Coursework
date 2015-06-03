root<-function(){
#1. (-1)^1/2 (Note: NaN stands for “Not a Number”)
x<-(-1)^(1/2)
x
}

decreasing<-function(){
#2.The vector consisting of the decreasing sequence of consecutive integers from 57 to –11
v<-c(57:-11)
v
}

odd<-function(){
#3. The vector consisting of the increasing sequence of odd integers from –11 to 57. Hint: See seq

v1<-seq(-11,57,2,2)
v1
}

alternating<-function(){
#4. The vector consisting of five hundred alternating zeros and ones. Hint: See rep
vector<-c(0:1)
rep.int(vector,500)
}

average<-function(){
#5. The average of 12.7, 9.4, 6.6, 10.8, 5.3, and 7.2. Hint: See mean
m<-c(12.7, 9.4, 6.6, 10.8, 5.3,7.2)
mean(m)
}

sort<-function(){
#6.Sort the six preceding numbers in decreasing order. Hint: See sort
m<-c(12.7, 9.4, 6.6, 10.8, 5.3,7.2)
sort(m,decreasing = T)
}
uniform<-function(){

#7. A vector of fifty, uniformly distributed, random values between – 1 and +1. Hint: See runif
m<-c(1:50)
runif(m, min = -1, max = 1)
}

subset<-function(){
#.8 The vector consisting of positive values from the preceding vector. Hint: See subset
v<-c(57:-11)
v2<-subset(v,v>0)
v2
}

position<-function(){
#9. The positions of the positive values in the original vector. Hint: See which
w<-c(1,-3,4,5,6,-9,-2,2,2)
z=which(w > 0)
z
}

PerfectSquare<-function(){
#10. The vector of the first 1000 positive integers, without the perfect squares.
i=c(1:1000)
p=i*i
i[-p]
}





