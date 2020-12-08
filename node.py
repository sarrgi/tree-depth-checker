class Node:

    def __init__(self, name):
        self.name = name
        self.parent = -1
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def set_children(self, children):
        self.children = children

    def set_parent(self, parent):
        self.parent = parent

    # def to_string(self):
    #     return self.name + " : " + self.children
