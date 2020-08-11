i = int(input())
for x in range(i):
    if x < i:
        print(" "*((i-1)-x)+"*"*(x*2+1))