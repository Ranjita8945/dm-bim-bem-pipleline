from math import sqrt

def distance(p1, p2):
    """Compute Euclidean distance between two 3D points."""

    return sqrt(
        (p1[0] - p2[0])**2 +
        (p1[1] - p2[1])**2 +
        (p1[2] - p2[2])**2
    )


def are_adjacent(p1, p2, threshold=5.0):
    """
    Determine if two spaces are adjacent based on distance.
    threshold is in IFC model units (usually meters).
    """

    if None in p1 or None in p2:
        return False

    return distance(p1, p2) <= threshold