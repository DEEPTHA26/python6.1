u1,v1=map(int,input().split())
l=list(map(int,input().split()[:u1]))
count=0
for i in l:
   if(i==v1):
      count=count+1
print(count)      
