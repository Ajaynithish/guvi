n,a,d=map(int,input().split())
c=0
tot=0
while(c!=n):
    tot+=d
    d+=a
    c+=1
print(tot)
