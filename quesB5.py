# 5.Create an empty stack and push the values 5, 10, 15, 20 into it. Display
# the stack.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def display(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next


stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)

print("Stack (Top to Bottom):")
stack.display()    
        