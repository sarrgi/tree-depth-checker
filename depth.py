"""
TODO:
 - remove whitespaces
 - scalable parentheses
 - display tree
 - depth count
"""
import node
import re


def get_paren_locations(input):
    """
    Get the index loation of all paretheses of an input.

    Return:
        - left_positions: list off all indexes of left parenthese occurences.
        - right_positions: list off all indexes of left parenthese occurences.
    """
    left_positions = []
    right_positions = []

    for i, val in enumerate(input):
        if val == '(':
            left_positions.append(i)
        if val == ')':
            right_positions.append(i)

    return left_positions, right_positions


def get_pair_locations(left, right, max):
    """
    TODO: MAx value

    Get location of all parentheses pairs based on left and right lists.

    Return:
        - pairs: list of all parenthese pair locations.
    """
    pairs = []
    for l_pos in reversed(left):
        # find corresponding r_pos
        r_pos = max
        for r in right:
            if r < r_pos and r > l_pos:
                r_pos = r
        # add pair to list and remove from input lists
        pairs.append((l_pos, r_pos))
        left.remove(l_pos)
        right.remove(r_pos)

    return pairs


def is_value(text):
    """
    TODO: - not recheck parens here.

    Determine if a text string is a value (not a node at all).
    Will be a value if it only has no parentheses.
    """
    l, r = get_paren_locations(text)
    return len(l) == 0 and len(r) == 0


def is_leaf_node(text):
    """
    TODO: - not recheck parens here.

    Determine if a text string is a leaf node.
    Will be a leaf node if it only has a single set of parentheses.
    """
    l, r = get_paren_locations(text)
    return len(l) == 1 and len(r) == 1


def split_children_string(text):
    """
        TODO:
            - pass through delim and bracket types
    """
    paren_balance = 0
    split_locs = [0]
    for i, val in enumerate(text):
        if val == '(':
            paren_balance += 1
        elif val == ')':
            paren_balance -= 1
        elif val == ',' and paren_balance == 0:
            # found a child splitting point
            split_locs.append(i+1)

    # split into children based on index location
    children = [text[i:j] for i,j in zip(split_locs, split_locs[1:]+[None])]
    # strip delim at end of all but last child
    children = [x.strip(",") for x in children]

    return children


def recursive_process(text):
    l, r = get_paren_locations(text)

    # create node
    n = node.Node(text[:l[0]])

    # check if leaf node
    if is_leaf_node(text):
        # get children
        leaf_text = text[l[0]+1:r[0]]
        children = leaf_text.split(",")
        # set children to nodes children
        n.set_children(children)
    else:
        # is not a leaf node
        # strip outer parens
        node_text = text[l[0]+1:-1]

        node_children = split_children_string(node_text)

        for c in node_children:
            if is_value(c):
                n.add_child(c)
            else:
                # get type of current node
                l, r = get_paren_locations(c)
                node_name = c[:l[0]]
                # create current node
                cNode = node.Node(node_name)
                # pass current node throguh recursive helper
                n.add_child(recursive_helper(n, cNode, c[l[0]:]))

    return n


def recursive_helper(parent, n, text):
    # set parent to nodes
    parent.add_child(n)

    if is_leaf_node(text):
        # get children
        l, r = get_paren_locations(text)
        leaf_text = text[l[0]+1:r[0]]
        children = leaf_text.split(",")
        # set children to nodes children
        n.set_children(children)

    else:
        # strip outer parens
        node_text = text[1:-1]
        node_children = split_children_string(node_text)

        for c in node_children:
            if is_value(c):
                n.add_child(c)
            else:
                # get type of current node
                l, r = get_paren_locations(c)
                node_name = c[:l[0]]
                # create current node
                ccNode = node.Node(node_name)
                # recusrivley add children
                n.add_child(recursive_helper(n, ccNode, c[l[0]:]))

    return node



if __name__ == "__main__":
    # load in file
    file = open("test_suite/test5.txt", "r")
    lines = file.read()

    # get positions of all parens
    left_positions, right_positions = get_paren_locations(lines)

    # get the root based on paren locations
    root_pos = (min(left_positions), max(right_positions))
    root_name = lines[:root_pos[0]]
    root = node.Node(root_name)

    # get string version of root children
    root_child_string = lines[root_pos[0]+1:root_pos[1]]
    root_children = split_children_string(root_child_string)

    # program raw printout
    print("------------------------------------------------")
    print(root.name, root_child_string)
    print("------------------------------------------------")

    # recursively find all children of root
    for c in root_children:
        cc = recursive_process(c)
        # print("CC:", cc)
        root.add_child(cc)

    # printout the root
    root.print_out(0)
