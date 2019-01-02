from typing import List
from .exceptions import ZeroHedgeRatioException, NilListException, MissMatchedLengthException

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
