# 7.Display the top element of the stack without removing it.
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

    def peek(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Top Element:", self.top.data)

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

stack.peek()