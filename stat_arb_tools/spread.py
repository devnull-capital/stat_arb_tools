from typing import List
from math import log
from .exceptions import ZeroHedgeRatioException, NilListException, MissMatchedLengthException
from .beta import calcBetaHat

ZeroQException = Exception("q cannot be zero")

def calcSpread(p: float, q: float, hedgeRatio: float) -> float:
    """Calculates the spread between two asset prices at time t.


    Parameters
    ----------
    p : float
        Price at time t of one of the two assets.
    q : float
        Price at time t of the other of the two assets.
    hedgeRatio : float
        The hedge ratio between the two assets.


    Returns
    -------
    float
        Returns the spread.

    """
    return (p - hedgeRatio * q)

def calcSpreadReturn(p: float, q: float, hedgeRatio: float) -> float:
    """Calculates the spread return between two asset prices at time t.


    Parameters
    ----------
    p : float
        Price at time t of one of the two assets.
    q : float
        Price at time t of the other of the two assets.
    hedgeRatio : float
        The hedge ratio between the two assets.


    Returns
    -------
    float
        Returns the spread return.


    Raises
    ------
    ZeroHedgeRatioException
        If the hedge ratio is zero.
    ZeroQException
        If Q is zero.

    """
    if hedgeRatio == 0:
        raise ZeroHedgeRatioException
    if q == 0:
        raise ZeroQException

    return ((p - hedgeRatio * q) / (hedgeRatio * q))

def calcDist(zX: List[float], zY: List[float]) -> float:
    """Calculates the sum of squared differences between two normalized price series. Normalization should be done through the z-transform.


    Parameters
    ----------
    zX : list of float
        Normalized list of asset #1
    zY : list of float
        Normalized list of asset #2


    Returns
    -------
    float
        Returns the sum of squared differences.


    Raises
    ------
    NilListException
        If a list of length zero is provided.
    MissMatchedLengthException
        If the lists are not of equal length.

    """
    if len(zX) == 0:
        raise NilListException
    if len(zX) != len(zY):
        raise MissMatchedLengthException

    dist = 0.0
    for i in range(len(zX)):
        dist += (zX[i] - zY[i]) ** 2

    return dist

def calcNotes(l1: List[float], l2: List[float]) -> List[float]:
    """At time t, the log price difference (spread) is a random variable ut plus a constant ln(𝛽). This function calculates those random variables, ut.


    Parameters
    ----------
    l1 : list of float
        Time series of prices of asset #1.
    l2 : list of float
        Time series of prices of asset #2.



    Returns
    -------
    list of float



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

    betaHat = calcBetaHat(l1, l2)

    ut = []
    for i in range(len(l1)):
        ut.append(log(l1[i]) - log(l2[i]) - log(betaHat))

    return ut
