inp=int(input())
arr=[int(x) for x in input().split()[:inp]]
rra=sorted(arr,reverse=True)
tot=0
for i in range(0,int(len(rra))):
    tot=(tot*10)+rra[i]
print(tot)
