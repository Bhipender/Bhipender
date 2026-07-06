# 8.Check whether a stack is empty and display an appropriate message.
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

    def is_empty(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")


stack = Stack()

stack.is_empty()

stack.push(5)
stack.push(10)

stack.is_empty()