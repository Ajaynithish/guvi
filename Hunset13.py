inp=int(input())
lee=[int(x) for x in input().split()[:inp]]
nlee=[]
for i in range(0,int(len(lee))):
    if(i==lee[i]):
        nlee.append(i)
if(int(len(nlee)))!=0:
    for u in nlee:
        print(u,end=" ")
else:
    print(-1)
