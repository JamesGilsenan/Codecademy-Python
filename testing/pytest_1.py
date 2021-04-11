"""An example of a Python module"""

"""This is a skeleton function. Returns a dummy, the correct type"""
def total(xs: [float]) -> float :
    """Total returns the sum of xs"""
    result: float = 0.0
    # for each x float in xs, add it to result
    for x in xs:
        result += x
    return result


def join(xs: [int], delimiter: str) -> str:
    """Produce a string where subsquent items are seperated by delimiter"""
    result = ""

    for x in xs:
        if result == "": # Don't put delimiter before first value
            result = str(x)
        else:
            result += delimiter + str(x)
    return result