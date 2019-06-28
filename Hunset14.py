aj=int(input())
lee=[int(x) for x in input().split()[:aj]]
for u in lee:
    if(lee.count(u)==1):
        print(u,end=" ")
