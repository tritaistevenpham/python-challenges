def min_four(x: int, y: int, z: int, w: int) -> int:
    # Imports Integers and Returns an Integer
    # Returns the minimum of the four given integers
    # Examples:
    #   min_four(1, 2, 3, 4) -> 1
    #   min_four(3, 2, 4, 6) -> 2
    #   min_four(0, 0, -5, 0) -> -5
    minimum: int = x
    if minimum >= y:
        minimum = y
    if minimum >= z:
        minimum = z
    if minimum >= w:
        minimum = w
    return minimum
