inp=int(input())
if(inp%400==0):
    print("Yes")
elif(inp%4==0 and inp%100!=0):
    print("yes")
else:
    print("no")
