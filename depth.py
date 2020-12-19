import node

import re
import sys


def get_paren_locations(input, parens):
    """
    Get the index loation of all paretheses of an input.

    Return:
        - left_positions: list off all indexes of left parenthese occurences.
        - right_positions: list off all indexes of left parenthese occurences.
    """
    left_positions = []
    right_positions = []

    for i, val in enumerate(input):
        if val == parens[0]:
            left_positions.append(i)
        if val == parens[1]:
            right_positions.append(i)

    return left_positions, right_positions


def is_value(text, parens):
    """
    TODO: - not recheck parens here.

    Determine if a text string is a value (not a node at all).
    Will be a value if it only has no parentheses.
    """
    l, r = get_paren_locations(text, parens)
    return len(l) == 0 and len(r) == 0


def is_leaf_node(text, parens):
    """
    TODO: - not recheck parens here.

    Determine if a text string is a leaf node.
    Will be a leaf node if it only has a single set of parentheses.
    """
    l, r = get_paren_locations(text, parens)
    return len(l) == 1 and len(r) == 1


def split_children_string(text, parens, separator):
    """
        TODO:
            - pass through delim and bracket types
    """
    paren_balance = 0
    split_locs = [0]
    for i, val in enumerate(text):
        if val == parens[0]:
            paren_balance += 1
        elif val == parens[1]:
            paren_balance -= 1
        elif val == separator and paren_balance == 0:
            # found a child splitting point
            split_locs.append(i+1)

    # split into children based on index location
    children = [text[i:j] for i,j in zip(split_locs, split_locs[1:]+[None])]
    # strip delim at end of all but last child
    children = [x.strip(separator) for x in children]

    return children


def remove_whitespace(text):
    return re.sub("\s", "", text)


def recursive_process(text, separator, parens, indent_style):
    l, r = get_paren_locations(text, parens)

    # create node
    n = node.Node(text[:l[0]], indent_style)

    # check if leaf node
    if is_leaf_node(text, parens):
        # get children
        leaf_text = text[l[0]+1:r[0]]
        children = leaf_text.split(separator)
        # set children to nodes children
        n.set_children(children)
        # set to leaf node
        n.set_leaf(True)
    else:
        # is not a leaf node
        # strip outer parens
        node_text = text[l[0]+1:-1]

        node_children = split_children_string(node_text, parens, separator)

        for c in node_children:
            if is_value(c, parens):
                n.add_child(c)
            else:
                # get type of current node
                l, r = get_paren_locations(c, parens)
                node_name = c[:l[0]]
                # create current node
                cNode = node.Node(node_name, indent_style)
                # pass current node throguh recursive helper
                n.add_child(recursive_helper(n, cNode, c[l[0]:], separator, indent_style))

    return n


def recursive_helper(parent, n, text, separator, indent_style):
    # set parent to nodes
    parent.add_child(n)

    if is_leaf_node(text, parens):
        # get children
        l, r = get_paren_locations(text, parens)
        leaf_text = text[l[0]+1:r[0]]
        children = leaf_text.split(separator)
        # set children to nodes children
        n.set_children(children)
        # set to leaf node
        n.set_leaf(True)

    else:
        # strip outer parens
        node_text = text[1:-1]
        node_children = split_children_string(node_text, parens, separator)

        for c in node_children:
            if is_value(c, parens):
                n.add_child(c)
            else:
                # get type of current node
                l, r = get_paren_locations(c, parens)
                node_name = c[:l[0]]
                # create current node
                ccNode = node.Node(node_name, indent_style)
                # recusrivley add children
                n.add_child(recursive_helper(n, ccNode, c[l[0]:], separator, indent_style))

    return node


def build_tree(input, parens, separator, indent_style):
    """
    Build entire tree based on program input.
    """
    # get positions of all parens
    left_positions, right_positions = get_paren_locations(input, parens)

    # get the root based on paren locations
    root_pos = (min(left_positions), max(right_positions))
    root_name = input[:root_pos[0]]
    root = node.Node(root_name, indent_style)

    # get string version of root children
    root_child_string = input[root_pos[0]+1:root_pos[1]]
    root_children = split_children_string(root_child_string, parens, separator)

    # program raw printout
    # print("------------------------------------------------")
    # print(root.name, root_child_string)
    # print("------------------------------------------------")

    # edge case check for tree where root is the only node
    if [is_value(x, parens) for x in root_children][0]:
        root.set_children(root_children)
        return root

    # recursively find all children of root
    for c in root_children:
        root.add_child(recursive_process(c, separator, parens, indent_style))

    return root



def max_depth(n, depth):
    """

    """
    if n.is_leaf:
        return depth
    else:
        children_depth = []
        for c in n.children:
            if type(c) == node.Node:
                children_depth.append(max_depth(c, depth + 1))
            # else:
            #     children_depth.append(depth+1)

        if len(children_depth) > 0:
            return max(children_depth)
        else:
            return 0

    return -1


def min_depth(n, depth):
    """

    """
    if n.is_leaf:
        return depth
    else:
        children_depth = []
        for c in n.children:
            if type(c) == node.Node:
                children_depth.append(min_depth(c, depth + 1))
            # else:
            #     children_depth.append(depth+1)

        if len(children_depth) > 0:
            return min(children_depth)
        else:
            return 0

    return -1



def parse_arg(arg):
    """
    Parses each user inputted argument.

    Returns:
        - arg_type (`str`) : string keyword representing the argument type which user is changing.
        - arg_val (`str`) : string value for the corresponding argument type user is changing.

    Raises Exceptions if user enters incorrect parameter argument.
    """
    # split argument
    arg_split = arg.split("=")

    # check split was correct
    if len(arg_split) != 2:
        raise Exception("Error parsing parameter: " + arg)

    arg_type = arg_split[0]
    arg_val = arg_split[1]

    # parse user argument
    if arg_type == "left" or arg_type == "left_paren" or arg_type == "l":
        return "left_paren", arg_val
    elif arg_type == "right" or arg_type == "right_paren" or arg_type == "r":
        return "right_paren", arg_val
    elif arg_type == "sep" or arg_type == "separator" or arg_type == "s":
        return "separator", arg_val
    elif arg_type == "indent" or arg_type == "indent_style" or arg_type == "i":
        return "indent_style", arg_val
    elif arg_type == "file" or arg_type == "file_name" or arg_type == "f":
        return "file_name", arg_val

    # user has entered an unknown argument
    raise Exception("Unknown parameter: " + arg_type)


def tree_params_config(arguments):
    """
    Configuration process for setting up the parameteres of the tree.
    Handles user input for setting the parameters, and uses default values if not specified by the user.

    Args:
        - arguments (`list` of `str`) : list of user command line arguments

    Return:
        - parens (('str', `str`)) : tuple of parentheses types. ("left", "right")
        - separator (`str`) : value for separator in tree.
    """
    # set up default config
    left_paren = '('
    right_paren = ')'
    separator = ','
    indent_style = "->"
    file_name = "output.txt"

    if len(sys.argv) > 1:
        for arg in sys.argv[2:]:
            arg_type, arg_val = parse_arg(arg)
            if arg_type == "left_paren": left_paren = arg_val
            elif arg_type == "right_paren": right_paren = arg_val
            elif arg_type == "separator": separator = arg_val
            elif arg_type == "indent_style": indent_style = arg_val
            elif arg_type == "file_name": file_name = arg_val
    else:
        # let user know they are using default settings
        print("--------------------------------",
              "\nRunning with default parameters:",
              "\nLeft Parentheses:", left_paren,
              "\nRight Parentheses:", right_paren,
              "\nSeparator:", separator,
              "\nIndent Style:", indent_style,
              "\nFile Name:", file_name,
              "\n--------------------------------")
        return (left_paren, right_paren), separator, file_name, indent_style

    # let user know custom settings have been applied
    print("--------------------------------",
          "\nRunning with parameters:",
          "\nLeft Parentheses:", left_paren,
          "\nRight Parentheses:", right_paren,
          "\nSeparator:", separator,
          "\nIndent Style:", indent_style,
          "\nFile Name:", file_name,
          "\n--------------------------------")

    return (left_paren, right_paren), separator, file_name, indent_style



if __name__ == "__main__":
    # set up tree config
    parens, separator, out_file_name, indent_style = tree_params_config(sys.argv)
    file_path = sys.argv[1]

    # load in file
    file = open(file_path, "r")
    input = file.read()
    # pre-process whitespace
    input = remove_whitespace(input)

    # build tree
    root = build_tree(input, parens, separator, indent_style)

    # calculate max depth of tree
    max_depth = max_depth(root, 0)

    # printout the tree from the root
    root.print_out(0)

    # save the tree printout to a file
    root.print_to_file(out_file_name)
    # save the depth printout to the same file
    output_file = open(out_file_name, "a")
    output_file.write("".join(("-----------------------------------------\nMax Depth:", str(max_depth))))


    print("Depth:", max_depth)
