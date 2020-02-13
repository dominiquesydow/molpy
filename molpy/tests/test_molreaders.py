import numpy as np
import pytest

import molpy


@pytest.mark.parametrize("molecule, cog, natoms", [("water", [9.81833333, 7.60366667, 12.673], 3),
                                                   ("benzene", [-1.4045, 0, 0], 12)])
def test_read_xyz(molecule, cog, natoms):

    mol = molpy.data.get_molecule(molecule)
    print(np.mean(mol["geometry"], axis=0))
    print(cog)
    assert np.allclose(np.mean(mol["geometry"], axis=0), cog)
    assert len(mol["geometry"]) == natoms
    assert len(mol["symbols"]) == natoms


@pytest.mark.parametrize("molecule", [("unknown")])
def test_read_xyz_exception(molecule):

    with pytest.raises(FileNotFoundError):
        molpy.data.get_molecule(molecule)
