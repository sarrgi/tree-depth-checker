"""
TODO:
 - remove whitespaces
 - scalable parentheses
 - display tree
 - depth count
"""

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
    Note: Assumes len(left) == len(right).

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

if __name__ == "__main__":
    # load in file
    file = open("test_suite/test3.txt", "r")
    lines = file.read()

    left_positions, right_positions = getParenLocations(lines)
    # pairs = getPairLocations(left_positions, right_positions, 100000000000)

    # print(left_positions)
    indent = 0
    for i, val in enumerate(lines):
        if i in left_positions:
            # print(":",i,":", sep="", end="")
            indent += 1
            print((indent * " -"), "\n", val, end="")
        elif i in right_positions:
            indent -= 1
            print(val,"\n" ,sep="", end="")
        else:
            print(val, sep="", end="")
