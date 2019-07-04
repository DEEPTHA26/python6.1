most8=list(input())
if len(most8)%2==0:
    most8[int(len(most8)/2)] ='*'
    most8[int(len(most8)/2)-1]='*'
else:
    most8[int(len(most8)/2)] ='*'
for i in range(0,len(most8)):
    print(most8[i],end='')
