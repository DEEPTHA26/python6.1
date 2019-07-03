ob=input()
for i in range(0,len(ob)):
   if(ob[i].isalpha() and ob[i].isdigit()):
    print("No")
else:
  print("Yes")
