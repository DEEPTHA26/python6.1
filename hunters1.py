values8=list(map(int,input().split()))   
final=[]
for val in values8:
    if values8.count(val)>1:
        if str(val) not in final:
            final.append(str(val))
if len(final)!=0:
    final.sort()
    print(" ".join(final))   
else:
    print("unique")
