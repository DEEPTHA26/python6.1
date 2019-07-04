m1,u1=map(int,input().split())
l=list(map(int,input().split()[:m1]))
count=0
for i in l:
   if(i==u1):
      print("yes")
      break
else:
   print("no")
