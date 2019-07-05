ld=int(input())
l=list(map(int,input().split()))
lg=l[0]
if ld==len(l):
  for i in range(1,len(l)):
    if l[i]>lg:
      lg=l[i]
    else:
      print(i-1)
      break
