def quadrilateral_type(a, b, c, d):
    if a == b == c == d:
        return "rhombus"
    elif a == c and b == d:
        return "parallelogram"
    else:
        return "neither"
