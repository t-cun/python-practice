# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class stackNode:
    def __init__(self, dataval = None, currentMin = None):
        self.dataval = dataval
        self.nextval  = None
        self.nextmin = currentMin

class stack:
    def __init__(self):
        self.headval = None
        self.minval = None

    def pop(self):
        top = self.headval.dataval
        self.minval = (self.minval, self.headval.nextmin)[top == self.minval]
        self.headval = self.headval.nextval
        return top

    def push(self, val):
        newNode = stackNode(val, self.minval)
        if self.minval is None:
            self.minval = val
        else:
            self.minval = (self.minval, val)[val < self.minval]

        newNode.nextval = self.headval
        self.headval = newNode

    def min(self):
        return self.minval

def printList(llist):
    currentNode = llist.headval

    niceList = f'[ '
    while currentNode != None:
        niceList += f' {currentNode.dataval}, '
        currentNode = currentNode.nextval
    print(niceList + ']')

list1 = stack()
printList(list1) # empty list

list1.push(2)
list1.push(1)
list1.push(6)
list1.push(0)
list1.push(6)
list1.push(6)
list1.push(6)
list1.push(-1)

printList(list1)
print(f'min(list1) = {list1.min()}\n')

print(f'popped {list1.pop()}')
print(f'popped {list1.pop()}\n')
printList(list1)
print(f'min(list1) = {list1.min()}\n')

print(f'popped {list1.pop()}')
print(f'popped {list1.pop()}')
print(f'popped {list1.pop()}\n')

printList(list1)
print(f'min(list1) = {list1.min()}\n')

print(f'popped {list1.pop()}')
print(f'popped {list1.pop()}\n')

printList(list1)
print(f'min(list1) = {list1.min()}\n')

print(f'popped {list1.pop()}\n')
printList(list1)
print(f'min(list1) = {list1.min()}')