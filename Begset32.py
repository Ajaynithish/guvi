s=int(input())
arr=list(map(int,input().split()[:s]))
rra=sorted(arr,reverse=True)
print(rra[0])
