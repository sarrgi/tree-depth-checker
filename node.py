class Node:

    def __init__(self, name):
        self.is_leaf = False
        self.name = name
        self.parent = -1
        self.children = []

    def add_child(self, child):
        """
        Add a child to node's current children
        """
        # Has a check to stop class 'module' nodes appearing
        if type(child) == Node or type(child) == str:
            self.children.append(child)

    def set_children(self, children):
        "Set the children of the node."
        self.children = children

    def set_parent(self, parent):
        """
        Set the parent of the node.
        """
        self.parent = parent

    def set_leaf(self, val):
        self.is_leaf = val

    def print_out(self, indent_level):
        """
        TODO:
            - stylable params

        Recursively printout a node and all of it's children.
        """
        # printout current node
        print("".join((indent_level * "   ", "-> ", self.name)), sep="", end="\n")

        # print(self.name, len(self.children))

        for c in self.children:
            if type(c) == Node:
                # recurse through nodes children
                c.print_out(indent_level+1)
            else:
                # avoid module type occurences - TODO: find why these exist
                if type(c) != str:
                    print("".join(((indent_level+1) * "   ", "-> ", "WARN", str(indent_level+1))))
                    continue
                # print("FINE", type(c), c)
                 # printout current value
                print("".join(((indent_level+1) * "   ", "-> ", c)), sep="", end="\n")




    # def find_max_depth(self):
    #     depths = []
    #
    #     for c in self.children:
    #         depths.append(c.find_max_depth(1))
    #
    #     return max(depths)
    #
    # def find_max_depth(self, depth):
    #     if self.type == Node:
    #         # recurse
    #     else:
    #         # store value
    #
    #
    #     return -1
