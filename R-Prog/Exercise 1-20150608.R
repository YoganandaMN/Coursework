#Write a program to arrange a group of twenty people into a list of ten random pairs.
#Use the following general "pseudo-code" as a guide.
#Step 1. Label the group of integers {1, 2, 3, 4, ., 20}, and set mylist = NULL.
#Step 2. Run through the following "for" loop ten times:
#  . Randomly select one pair of integers from the group, without replacement.
#(Hint: See sample)
#. Adjoin this pair of integers to mylist as a new row. (Hint: See rbind)
#. Remove this pair from the remaining integers in the group. (Hint: See which)
#Step 3. Output mylist.

v<-c(1:20)
v
Mylist<-list()
#rbind<-rbind(NULL)
for(i in 1:10){
  sa<-sample(c(1:20),2,replace = FALSE)
 # Mylist[[length(Mylist)+1]]<-rbind(sa,deparse.level = 0)
 Mylist<-rbind(Mylist,sa,deparse.level = 0)
  }
#Mylist[[1]]=NULL
Mylist
