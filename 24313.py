#백준 24313

a1 , a0 = map(int,input().split())
c = int(input())
n0 = int(input())

c1 = a1*n0 + a0
g1 = c*n0
if a1 > c :
    print(0)
else :
    if g1 >= c1 : print(1)
    else : print(0)
