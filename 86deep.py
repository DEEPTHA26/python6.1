o=list(input())
i=[]
for j in o:
   if j not in i:
      i.append(j)
if o==i:
   print("Yes")
else:
   print("No")
