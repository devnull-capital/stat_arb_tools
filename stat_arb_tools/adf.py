from statsmodels.tsa.stattools import adfuller
from .beta import calcBetaHat
from .exceptions import NilListException, MissMatchedLengthException
from math import log
from typing import List, Tuple

def adf(l1: List[float]) -> Tuple[float, float]:
    """Runs the augmented Dickey-Fuller test.


    Parameters
    ----------
    l1 : list of float
        Time series of ut hat.


    Returns
    -------
    tuple of float
        Returns the statistic and pVal


    Raises
    ------
    NilListException
        If a list of length zero is provided.

    """
    if len(l1) == 0:
        raise NilListException

    result = adfuller(l1)

    # statistic, pVal
    return result[0], result[1];

def isStationary(l1: List[float], l2: List[float]) -> Tuple[float, float]:
    """Runs the augmented Dickey-Fuller test on two time series of asset prices.


    Parameters
    ----------
    l1 : list of float
        Time series of prices of asset #1.
    l2 : list of float
        Time series of prices of asset #2.


    Returns
    -------
    tuple of float
        Returns the statistic and pVal


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

    return adf(ut)
