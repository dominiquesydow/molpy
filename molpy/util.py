import numpy as np

def distance(point1, point2):
    """
    Calcuate distance between two points.

    Parameters
    ----------
    point1 : array_like
        The first point.
    point2 : array_like
        The second point.

    Returns
    -------
    float
        The distance between point1 and point2.

    """

    point1 = np.asarray(point1)
    point2 = np.asarray(point2)

    return np.linalg.norm(point1 - point2)


def open_xyz(file_location):
    """
    Open an xyz file and return symbols and coordinates.

    Parameters
    ----------
    file_location : str
        Location to xyz file.

    Returns
    -------
    tuple (numpy.ndarray, numpy.ndarray)
        Symbols and coordinates for atoms in xyz file.
    """
    
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coords = (xyz_file[:,1:])
    coords = coords.astype(np.float)

    return symbols, coords
