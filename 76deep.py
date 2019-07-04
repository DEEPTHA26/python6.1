f8=int(input())
if(f8>1):
   for i in range (2,f8):
      if(f8%i==0):
       print("yes")
       break
   else:
      print("no")
