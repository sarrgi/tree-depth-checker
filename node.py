class Node:

    def __init__(self, name):
        self.name = name
        self.parent = -1
        self.children = []

    def add_child(self, child):
        self.children.append(child)
