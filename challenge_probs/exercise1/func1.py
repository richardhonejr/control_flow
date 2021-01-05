"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: YOUR NAME HERE
Date: THE DATE HERE
"""
import introcs


def findall(text, sub):
    """
    Returns the tuple of all positions of substring sub in text.

    If sub does not appears anywhere in text, this function returns the empty tuple ().

    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)

    Parameter text: The text to search
    Precondition: text is a string

    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    # pass

    # create an empty tuple to hold the results
    tup = ()
    x = 0
    halted = False

    # create a loop that advances through the index positions in text
    while halted is False:
        results = introcs.find_str(text, sub, x)

        if results != -1:
            tup += (results,)
        else:
            halted = True
        x = results + 1

    return tup
