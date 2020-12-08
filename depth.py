"""
TODO:
 - remove whitespaces
 - scalable parentheses
 - display tree
 - depth count
"""
import node
import re

def getParenLocations(input):
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


def getPairLocations(left, right, max):
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

def inititialTextSplit(sep):
    """
    TODO:
    - based on https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators?lq=1
    """
    # seperate text
    children = [x+sep for x in lines[root_pos[0]:].split(sep)]
    # remove sep from final obj
    children[-1] = children[-1].strip(sep)

    # strip root parenthese from start and end child
    children[0] = children[0][1:]
    children[-1] = children[-1][:-2]

    return children


def convertChild(child):
    n = None
    parens = getParenLocations(child)

    # is a leaf node
    if len(parens[0]) == 1:
        # get node name
        n = node.Node(child[:parens[0][0]])
        # get node children
        children = (child[parens[0][0]+1:parens[1][0]]).split(",")
        for c in children:
            n.add_child(c)
    # is not a leaf Node
    else:
        n = node.Node(child[:parens[0][0]])

        child_text = child[parens[0][0]:]
        # # strip end parentheses
        # child_text = child_text[1:-1]
        converterHelper(n, child_text)

        # print(n.name)
        # print(child_text)

    return n

def converterHelper(node, text):
    # split text based
    first_split = text.split(',', maxsplit=1)

    left_l,left_r = getParenLocations(first_split[0])
    right_l,right_r = getParenLocations(first_split[1])

    print(first_split)
    # handle left split
    if len(left_l) == 1:
        # issa root
        c = first_split[0][1:]
        node.add_child(c)
    else:
        # c_node = f
        print(first_split[1])
        # converterHelper()

    #     recurse
    print("??", first_split[1])
    # if len(r) == 1:
    #     # issa root
    # l,r = getParenLocations(first_split[1])
    # print(getPairLocations(l, r, 100000000))

    return -1






def isLeafNode(text):
    """
    Determine if a text string is a leaf node.
    Will be a leaf node if it only has a single set of parentheses.
    """
    l, r = getParenLocations(text)
    return len(l) == 1 and len(r) == 1


def splitChildrenString(text):
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


def yaya(text):

    l, r = getParenLocations(text)


    return -1

if __name__ == "__main__":

    # load in file
    file = open("test_suite/test3.txt", "r")
    lines = file.read()

    left_positions, right_positions = getParenLocations(lines)

    # get the root
    root_pos = (min(left_positions)+1, max(right_positions))
    root_name = lines[:root_pos[0]]
    root = node.Node(root_name)


    root_child_string = lines[root_pos[0]:root_pos[1]]
    print(root_child_string)
    print("---------------")

    root_children = splitChildrenString(root_child_string)

    for i in root_children:
        # could add to root if a leaf node?
        print(i, isLeafNode(i))
        if not isLeafNode(i):
            yaya(i)




    # get root children
    # root_children = inititialTextSplit(sep="),")
    # for child in root_children:
    #     root.add_child(child)
    #
    # print(root_children)

    # for child in root_children:
    #     n = convertChild(child)

        # printout
        # if type(n) == node.Node:
        #     root.add_child(n)
        #     print(n.name, n.children)
        # else:
        #     print("none")
    # recurse through children
    # print(root.name, root.children)




    # pairs = getPairLocations(left_positions, right_positions, 100000000000)

    # indent = 0
    # for i, val in enumerate(lines):
    #     if i in left_positions:
    #         # print(":",i,":", sep="", end="")
    #         indent += 1
    #         print((indent * " -"), "\n", val, end="")
    #     elif i in right_positions:
    #         indent -= 1
    #         print(val,"\n" ,sep="", end="")
    #     else:
    #         print(val, sep="", end="")
