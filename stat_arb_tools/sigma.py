from math import log, sqrt
from typing import List
from .exceptions import NilListException, MissMatchedLengthException, ZeroHedgeRatioException

L2ZeroValException = Exception("a zero value in l2")
BetaHatLTEZeroException = Exception("beta hat is negative")

def calcSigmaHat(l1: List[float], l2: List[float], betaHat: float) -> float:
    """Calculates sigma hat (squared).


    Parameters
    ----------
    l1 : list of float
        Time series list of prices of asset #1.
    l2 : list of float
        Time series list of prices of asset #2. 
    betaHat : float
        Beta hat of the two asset series.


    Returns
    -------
    float
        Returns sigma hat (squared). 


    Raises
    ------
    NilListException
        If a list of length zero is provided.
    MissMatchedLengthException
        If the lists are not of equal length.
    L2ZeroValException
        If a zero value is present in l2.
    BetaHatLTEZeroException
        If beta hat is less than or equal to zero.

    """
    if len(l1) == 0:
        raise NilListException
    if len(l1) != len(l2):
        raise MissMatchedLengthException
    if betaHat <= 0:
        raise BetaHatLTEZeroException

    sigmaHat = 0.0
    for i in range(len(l1)):
        if l2[i] == 0:
            raise L2ZeroValException

        sigmaHat += ((log(l1[i] / l2[i])) ** 2)

    sigmaHat /= len(l1)

    sigmaHat -= ((log(betaHat)) ** 2)

    return sigmaHat

def calcEffectiveStandardDeviation(betaHat: float, hedgeRatio: float, sigmaHat: float) -> float:
    """Calculates effective standard deviation.


    Parameters
    ----------
    betaHat : float
        Beta hat of the two asset series.
    hedgeRatio : list of float
        The hedge ratio of two assets.
    sigmaHat : list of float
        The sigma hat of two assets.


    Returns
    -------
    float
        Returns the effective standard deviation.


    Raises
    ------
    ZeroHedgeRatioException
        If the hedge ratio is zero.

    """
    if hedgeRatio == 0:
        raise ZeroHedgeRatioException

    return sqrt(((betaHat ** 2) / (hedgeRatio ** 2)) * (sigmaHat + (3 / 2) * (sigmaHat ** 2)))
