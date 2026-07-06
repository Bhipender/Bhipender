# 6.Pop one element from the stack and display the updated stack
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

    def pop(self):
        if self.top is None:
            print("Stack is Empty")
            return

        popped = self.top.data
        self.top = self.top.next
        print("Popped Element:", popped)

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

stack.pop()

print("Updated Stack (Top to Bottom):")
stack.display()