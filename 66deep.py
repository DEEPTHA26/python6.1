deep=int(input())
if(deep>1):
   for i in range(2,deep):
      if(deep%i)==0:
         print("no")
         break
   else:
         print("yes")
 
else:
   print("no")
