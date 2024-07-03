def chebyshev_distance(p1, p2):
    """Docstring..."""
    return max(abs(x - y) for x, y in zip(p1, p2))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)


# First method
def chebyshev_distance(p1, p2):
    """Calculate Chebyshev distance using map and lambda."""
    return max(map(lambda x_y: abs(x_y[0] - x_y[1]), zip(p1, p2)))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)


# Second method
def chebyshev_distance(p1, p2):
    """Calculate Chebyshev distance using list comprehension."""
    return max([abs(p1[i] - p2[i]) for i in range(len(p1))])

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
