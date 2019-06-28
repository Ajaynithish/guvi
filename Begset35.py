s=int(input())
arr=list(map(int,input().split()[:s]))
rra=sorted(arr)
print(rra[(int(len(arr)))//2])
