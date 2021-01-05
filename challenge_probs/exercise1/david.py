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


    # richard's code
    tup = ()
    x = 0
    halted = False

    while halted is False:
        results = introcs.find_str(text, sub, x)
        print(results)

        if results != -1:
            tup += (results,)
        else:
            halted = True
        x = results + 1

    return tup


"""
    # code from David to test

    result = ()

    for x in range(len(text)):
        try:
            pos = introcs.index_str(text, sub, x)
            result = result + (pos,)
        except:
            result = result + ()
    return result
"""

"""
    # code from the image.png file from David
    result = ()

    i = 0

    while i < len(text):
        if sub not in text:
            result = result + ()
            i = i + 1
        else:
            pos = text.find(sub, i, -1)
            result = result + (pos,)
            i = i + ps + len(sub)
    return result
    """