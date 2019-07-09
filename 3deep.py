n26=int(input())
rev=0
while(n26>0):
    dig=n26%10
    rev=rev*10+dig
    n26=n26//10
print(rev)
