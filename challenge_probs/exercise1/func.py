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

    # code from the image.png file from David
    result = ()

    i = 0

    while i < len(text):
        if sub not in text:
            result = result + ()
            i = i + 1
            print(i)
        else:
            pos = text.find(sub, i, len(text) - 1)
            # print(pos)
            result = result + (pos,)
            print('before calc pos is ' + str(pos))
            print('this is i before calc ' + str(i))
            print('the length of sub is ' + str(len(sub)))
            i = i + pos + len(sub)
            print('i will advance to  ' + str(i))
    return result


"""
    # richard's code
    tup = ()
    x = 0
    halted = False

    while halted is False:
        results = introcs.find_str(text, sub, x)
        # print(results)

        if results != -1:
            tup += (results,)
        else:
            halted = True
        x = results + 1

    return tup
"""

"""
    # code from David to test
    # fixed

    result = ()

    for x in range(len(text)):
        # print(x)
        try:
            pos = introcs.index_str(text, sub, x)
            # print(pos)
            if pos not in result:
                result = result + (pos,)

        except:
            result = result + ()

    return result
"""
