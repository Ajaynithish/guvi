s=int(input())
arr=list(map(int,input().split()[:s]))
rra=sorted(arr)
for i in rra:
    print(i,end=" ")
