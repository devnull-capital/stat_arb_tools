from math import log, exp
from typing import List
from .exceptions import NilListException, MissMatchedLengthException

def calcBetaHat(l1: List[float], l2: List[float]) -> float:
    """Calculates beta hat.


    Parameters
    ----------
    l1 : list of float
        Time series list of prices of asset #1.
    l2 : list of float
        Time series list of prices of asset #2. 


    Returns
    -------
    float
        Returns beta hat. 


    Raises
    ------
    NilListException
        If a list of length zero is provided.
    MissMatchedLengthException
        If the lists are not of equal length.

    """
    if len(l1) == 0:
        raise NilListException
    if len(l1) != len(l2):
        raise MissMatchedLengthException

    b = 0.0
    for i in range(len(l1)):
        b += log(l1[i] / l2[i])

    return exp(b / len(l1))

def calcHedgeRatio(betaHat: float, sigmaHat: float) -> float:
    """Calculates the hedge ratio.


    Parameters
    ----------
    betaHat : float
        Beta hat of two assets.
    sigmaHat : float
        Sigma hat of two assets.


    Returns
    -------
    float
        Returns the hedge ratio.

    """
    return betaHat * (1 + 0.5 * sigmaHat)
