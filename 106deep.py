m,n=map(int,input().split())
lis8=input().split()
lj8=[]
for i in lis8:
  if (int(i)%2!=0):
    lj8.append(i)
print(lj8[n-1])
