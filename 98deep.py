deeptha=int(input())
l=list(map(int,input().split()))
guvi=l[0]
if deeptha==len(l):
  for i in range(1,len(l)):
    if l[i]>guvi:
      guvi=l[i]
    else:
      print(i-1)
      break
