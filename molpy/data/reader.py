import os

#from molpy import util
from molpy.util import open_xyz  
#from ..util import read_xyz

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'look_and_say.dat')

with open(filename, 'r') as handle:
    look_and_say = handle.read()

def get_molecule(molecule):
    """
    Get molecule symbols and geometry by molecule name.

    Parameters
    ----------
    molecule : str
        Molecule name.
    
    Returns
    -------
    dict
        Molecule symbols and geometry.
    """

    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, 'xyz', f'{molecule}.xyz')

    if not os.path.exists(filename):
        raise FileNotFoundError(f'File for molecule {molecule} does not exist.')

    return open_xyz(filename)

