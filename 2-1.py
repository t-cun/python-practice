# Write code to remove duplicates from an unsorted linked list

######### PROVIDED CODE #########

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Wed")
e5 = Node("Wed")
e6 = Node("Thurs")

list1.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6

######### MY CODE ######### - Start time 8:10pm 2/4/20

## Questions 
# Do we remove only the second instance or all instances of duplicated number? - assume only second instance
# Is this a singly or doubly linked list? Don't believe it matters yet.

# Possible solution 1:
# sort the list - could be done in O(n) after sorting and comparing == for val and next.val

# Possible solution 2:
# hash table of list - iterate and store, then remove along the way
# problems if needing to remove all instances of the duplicate (including 1st)

# Step 2 - removeDups([3, 5, 4, 3, 66, 7]) = [3, 5, 4, 66, 7]

def printList(llist):
    currentNode = llist.headval

    if not currentNode:
        return

    niceList = f'[ '
    while currentNode != None:
        niceList += f' {currentNode.dataval}, '
        currentNode = currentNode.nextval
    print(niceList + ']')



def removeDups(llist):

    # store the current values in a dict
    foundVals = {}

    # Create a node to iterate the list
    currentNode = llist.headval

    # and another to build a list without dups
    noDups = SLinkedList()

    ### We need to determine if we've seen the current value before
    while currentNode != None:
        if foundVals.get(currentNode.dataval):
            currentNode = currentNode.nextval
        else:
            print(currentNode.dataval)

            # Make a note that we've now seen this value
            foundVals[currentNode.dataval] = True

            # copy the node over to the new list - this adds to the front
            newNode = Node(currentNode.dataval)
            newNode.nextval = noDups.headval

            # The newest node goes to the front of the lsit
            noDups.headval = newNode
        
        # continue iterating the list
        currentNode = currentNode.nextval
    
    return noDups
                
printList(list1)
printList(list1)
printList(removeDups(list1))

### Finished at 8:42 - seems to work
# LinkedList from - https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
# Problems - was looking at dataval for 'None', not current node.
# Had to make printList function
# Didn't walk through my implementation conceptually before running some examples
# may matter, depending - my solution reverses the list
