# Nodes
# 1. Value - anything(strings, integers, objects)
# 2. The Next Node

class linkedListNode:
    def __init__(self, value, nextNode=None):
        # value is called a constructor 
        # constructor is a method that is called when an object is created
        self.value = value
        self.nextNode = nextNode

# "3" --> "7" --> "10"

node1 = linkedListNode("3")
node2 = linkedListNode("7")
node3 = linkedListNode("10")

node1.nextNode = node2 # node1 --> node2, "3" --> "7" 
node2.nextNode = node3 # node2 --> node3, "7" --> "10"

# node1 --> node2 --> node3

currentNode = node1

while True:
    print (currentNode.value, "-->", end=" "), 
    # end=" " --> this is used to place a space after the displayed string instead of a newline
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode



