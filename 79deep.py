o1,o2=map(int,input().split())
for u in range(0,(o1*o2)+1):
   if(u**2==0):
      print("yes")
      break
else:
   print("no")
