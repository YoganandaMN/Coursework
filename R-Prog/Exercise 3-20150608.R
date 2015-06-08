#Write an R program to first create a general random sample of ten uniformly
#distributed values between -50 and +50 (see runif), and sort them from lowest to highest.
#Imagine that these values represent the endpoints of nine adjacent intervals on the real line.
#Compute the midpoints of these nine intervals. Output the ten sorted values, and the midpoints.
RAndomFun<-function(){
for(i in 1:10){
  n<-runif(10,min = -50,max = 50)
  cat("Random Numbers\n")
  print(n)
  cat("\n")
  s<-sort.int(n)
  start=s[1]
  end=s[10]
  add=start+end
  midpoint=add/2
  cat("Sorted Values\n")
  print(s)
  mid="midpoint="
  #print (add)
  cat(mid,midpoint)
  cat("\n")
    
}
}