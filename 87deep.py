deepu1,sanju2=map(int,input().split())
n=1
while(n<=deepu1 and n<=sanju2):
   if(deepu1%n==0 and sanju2%n==0):
      cctv=n
   n=n+1
print(cctv)
