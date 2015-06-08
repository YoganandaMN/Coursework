#To generate Prime NUMbER
"Exercise 5: The Sieve of Eratosthenes is an ancient algorithm for generating prime numbers.???
{ , 3, 4 ,5, 6 , 7, 8 , 9, 10 2 ,11, 12 ,13, 14 ,15, } ???

Start with the integers {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,..}. Keep the first integer (2),
and delete every second integer following it, i.e., 4, 6, 8, 10, 12, 14, 16, 18, 20, etc.:
  . Next proceed to the next undeleted integer (3),
and delete every third integer following it, i.e., 6 (already deleted), 9, 12 (already deleted), 15, etc.:
{ , , 4 ,5, 6 , 7, 8 , 9 , 10 2 3 ,11, 12 ,13, 14 , 15 , } ??? . Then proceed to the next undeleted integer (5),
and delete every fifth integer following it, i.e., 10 (already deleted), 15 (already deleted), 20 (already
                                                                                                   deleted), 25, etc.), and so on. The integers that remain - {2, 3, 5, 7, 11, 13,.} - are the primes.
Write a short R program that duplicates this procedure, to generate all the prime numbers up to
(or including) any given integer n. Use the following general "pseudo-code" as a guide.
(Again, there may be multiple ways of doing this, using other commands.)
Step 1. For any admissible integer value "n = " input by the user, let integers denote the
initial sequence {2, 3, 4, ., n}.
Step 2. For any fixed k in integers, calculate which of them are to be deleted.
(Hint: These would correspond to multiples of k, i.e., a sequence up to n in steps of k,
 excluding k itself.)
Step 3. Set these integers to NA ("Not Available").
Step 4. When completed, locate where the remaining integers are; these are the primes.
(Hint: See is.na and !is.na)"


ToRemoveNA<-function(mylist){
  for(i in mylist){
    #print(i)
    if(!is.na(i)){
      print(i)
      #mylist[-i]
    }
    
  }
}


generateNA<-function(){
  mylist<-c()
  c<-2
  while(c<101){
  
    #print(c)
    cat("\n")
    i=c%%2
    if(c<=5 && c!=4)
    {
      mylist<-c(mylist,c)
    }
    else if(c%%2!=0 && c%%3!=0 && c%%5!=0 && c%%10!=0){
      mylist<-c(mylist,c)
    #print(c)
    }
    else{
    mylist<-c(mylist,NA)
    }
  c=c+1
}
#mylist
ToRemoveNA(mylist)
}



