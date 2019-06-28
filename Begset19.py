no,n=[int(y) for y in input().split()]
inp=[int(x) for x in input().strip().split()[:no]]
tot=0
for i in range(n):
    tot+=inp[i]
print(tot)
