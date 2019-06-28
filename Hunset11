aj=int(input())
lee=[int(x) for x in input().split()[:aj]]
nlee=[]
for x in range(0,int(len(lee))):
    for y in range(x+1,int(len(lee))):
        if(lee[x]==lee[y] and lee[x] not in nlee):
            nlee.append(lee[x])

if (int(len(nlee)))!=0:
    for i in sorted(nlee):
        print(i,end=" ")
else:
    print("unique")
