sanju=input()
n=0
for i in range(len(sanju)):
 if(sanju[i].isdigit() or sanju[i].isalpha() or sanju[i]==(" ")):
  continue
 else:
  n+=1
print(n)
