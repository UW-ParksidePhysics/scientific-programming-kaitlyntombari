"""
Read in two columns of data from a text file of arbitrary length.
"""

__author__ = "Kaitlyn Tombari"

import numpy as np


def read_two_columns_text(volumes_energies: str) -> np.ndarray:
    """Function used to read in two columns of data from a text file of arbitrary \
    length."""
    try: 
        data = np.loadtxt(volumes_energies).T
        return data
    except OSError as e:
        raise OSError(f"File {volumes_energies} cannot be found for reading.") from e


if __name__ == "__main__":
    filename = "volumes_energies.dat"
    try:
        data = read_two_columns_text(filename)
        print(f'{data=}, shape={data.shape}')
    except OSError as e:
        print(e)
        