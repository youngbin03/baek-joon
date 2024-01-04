import sys
a = int(sys.stdin.readline())
b = []
for i in range(a):
    arr = sys.stdin.readline().split()
    if(arr[0] == 'push'):
    	b.append(arr[1])
    elif(arr[0] == 'top'):
    	if not b:
    		print(-1)
    	else:
    		print(b[-1])
    elif(arr[0] == 'size'):
    	print(len(b))
    elif(arr[0] == 'empty'):
    	if not b:
    		print(1)
    	else:
    		print(0)
    elif(arr[0] == 'pop'):
    	if not b:
    		print(-1)
    	else:
    		print(b.pop())
