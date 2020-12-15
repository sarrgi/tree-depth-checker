class Node:
    """
    Node object class which represents a node in the equation tree.

    Params:
        - name (str) : The name of a node.
        - children (`list` of Nodes) : List of all children of a Node.
        - is_leaf (bool) : Flag for is a node is a leaf. True if leaf, False if not.
        - parent (TODO) : Not currently in use.
    """

    def __init__(self, name, indent_style):
        """
        Initiliazes a Node object with a name passed through.
        Children is  instantiated as a an empty list.
        Default value for Leaf is False.

        Params:
            - name (str) : The name of a node.
        """
        self.is_leaf = False
        self.name = name
        self.indent_style = indent_style
        self.children = []

    def add_child(self, child):
        """
        Add a child to node's current children.
        """
        # Has a check to stop class 'module' nodes appearing
        if type(child) == Node or type(child) == str:
            self.children.append(child)

    def set_children(self, children):
        """
        Set the children of the node.
        """
        self.children = children

    def set_parent(self, parent):
        """
        Set the parent of the node.
        """
        self.parent = parent

    def set_leaf(self, val):
        """
        Set the leaf value of a node.
        """
        self.is_leaf = val

    def print_out(self, indent_level):
        """
        Recursively printout a node and all of it's children.
        """
        # printout current node
        print("".join((indent_level * "   ", self.indent_style, " ", self.name)), sep="", end="\n")

        for c in self.children:
            if type(c) == Node:
                c.print_out(indent_level+1)
            else:
                print("".join(((indent_level+1) * "   ", self.indent_style, " ", c)), sep="", end="\n")


    def print_to_file(self, file_name):
        output_file = open(file_name, "w")
        self.recursive_file_write(output_file, 0)
        output_file.close()



    def recursive_file_write(self, file, indent_level):
        """
        Recursively printout a node and all of it's children.
        """
        # printout current node
        file.write("".join((indent_level * "   ", self.indent_style, " ", self.name, "\n")))

        # print(self.name, len(self.children))

        for c in self.children:
            if type(c) == Node:
                c.recursive_file_write(file, indent_level+1)
            else:
                file.write("".join(((indent_level+1) * "   ", self.indent_style, " ", c, "\n")))




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
