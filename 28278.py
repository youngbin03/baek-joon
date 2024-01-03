import sys
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,n):
        self.stack.append(n)

    def empty(self):
        if not self.stack: return 1
        else: return 0
    def pop(self):
        if self.empty():
            return -1
        return self.stack.pop()    
    def peek(self):
        if self.empty():
            return -1
        return self.stack[-1]   
    def get_size(self):
        return len(self.stack)

n = int(input())
c = Stack()
for i in range(n):
    com = list(map(int,sys.stdin.readline().split()))
    if com[0] == 1:
        c.push(com[1])
    else:
        if com[0] == 2: print(c.pop())
        if com[0] == 3: print(c.get_size())
        if com[0] == 4: print(c.empty())
        if com[0] == 5: print(c.peek())        
