import numpy as np
from typing import List
from .exceptions import NilListException

ZeroStdDevException = Exception("standard deviation is zero")

def zNorm(l: List[float]) -> List[float]:
    """Normalizes a list using the z-transform.


    Parameters
    ----------
    l : list of float
        Time series list of prices of asset.


    Returns
    -------
    list of float
        Returns the normalized list.


    Raises
    ------
    NilListException
        If a list of length zero is provided.
    ZeroStdDevException
        If a standard deviation is zero.

    """
    if len(l) == 0:
        raise NilListException

    std = np.std(l)
    if std == 0:
        raise ZeroStdDevException

    mean = np.mean(l)

    zL = np.array(l).astype(float)
    for i in range(len(zL)):
        zL[i] = ((zL[i] - mean) / std)

    return zL
