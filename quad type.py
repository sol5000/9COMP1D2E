def quadrilateral_type(a, b, c, d):
    if a == b == c == d:
        print("rhombus")
    elif a == c and b == d:
        print("parallelogram")
    else:
        print("neither")
