from enum import Enum
from math import log
from typing import List, Tuple, Optional
from statsmodels.tsa.stattools import adfuller, ResultsStore
from .beta import calcBetaHat
from .exceptions import NilListException, MissMatchedLengthException
from .spread import calcNotes

class Regression(Enum):
    c = "constant"
    ct = "constant and trend"
    ctt = "constant, and linear and quadratic trend"
    nc = "no constant and no trend"

class AutoLag(Enum):
    aic = "AIC"
    bic = "BIC"
    tstat = "t-stat"
    none = None

def adf(
    l1: List[float],
    maxlag: int = None,
    regression: Regression = Regression.c,
    autolag: AutoLag = AutoLag.aic,
    store: bool = False,
    regresults: bool = False
) -> Tuple[float, float, int, int, dict, float, Optional[ResultsStore]]:
    """Runs the augmented Dickey-Fuller test.


    Parameters
    ----------
    l1 : list of float
        Time series of ut hat.
    maxlag : int
        Maximum lag which is included in test, default 12*(nobs/100)^{1/4}
    regression : Regression enum
        Constant and trend order to include in regression

        - 'c' : constant only (default)
        - 'ct' : constant and trend
        - 'ctt' : constant, and linear and quadratic trend
        - 'nc' : no constant, no trend

    autolag : Autolag enum

        - if None, then maxlag lags are used
        - if 'AIC' (default) or ‘BIC’, then the number of lags is chosen to minimize the corresponding information criterion
        - 't-stat' based choice of maxlag. Starts with maxlag and drops a lag until the t-statistic on the last lag length is significant using a 5%-sized test

    store : bool
        If True, then a result instance is returned additionally to the adf 
    regresults : bool
        If True, the full regression results are returned. 

    Returns
    -------
    tuple of various values

        - adf (float) – Test statistic
        - pvalue (float) – MacKinnon’s approximate p-value based on MacKinnon (1994, 2010)
        - usedlag (int) – Number of lags used
        - nobs (int) – Number of observations used for the ADF regression and calculation of the critical values
        - critical values (dict) – Critical values for the test statistic at the 1 %, 5 %, and 10 % levels. Based on MacKinnon (2010)
        - icbest (float) – The maximized information criterion if autolag is not None.
        - resstore (ResultStore, optional) – A dummy class with results attached as attributes


    Raises
    ------
    NilListException
        If a list of length zero is provided.

    """
    if len(l1) == 0:
        raise NilListException

    return adfuller(l1, maxlag = maxlag, regression = regression.name, autolag = autolag.value, store = store, regresults = regresults)

def isStationary(
    l1: List[float],
    l2: List[float],
    maxlag: int = None,
    regression: Regression = Regression.c,
    autolag: AutoLag = AutoLag.aic,
    store: bool = False,
    regresults: bool = False
) -> Tuple[float, float, int, int, dict, float, Optional[ResultsStore]]:
    """Runs the augmented Dickey-Fuller test on two time series of asset prices.


    Parameters
    ----------
    l1 : list of float
        Time series of prices of asset #1.
    l2 : list of float
        Time series of prices of asset #2.
    maxlag : int
        Maximum lag which is included in test, default 12*(nobs/100)^{1/4}
    regression : Regression enum
        Constant and trend order to include in regression

        - 'c' : constant only (default)
        - 'ct' : constant and trend
        - 'ctt' : constant, and linear and quadratic trend
        - 'nc' : no constant, no trend

    autolag : Autolag enum

        - if None, then maxlag lags are used
        - if 'AIC' (default) or ‘BIC’, then the number of lags is chosen to minimize the corresponding information criterion
        - 't-stat' based choice of maxlag. Starts with maxlag and drops a lag until the t-statistic on the last lag length is significant using a 5%-sized test

    store : bool
        If True, then a result instance is returned additionally to the adf 
    regresults : bool
        If True, the full regression results are returned. 

    Returns
    -------
    tuple of various values

        - adf (float) – Test statistic
        - pvalue (float) – MacKinnon’s approximate p-value based on MacKinnon (1994, 2010)
        - usedlag (int) – Number of lags used
        - nobs (int) – Number of observations used for the ADF regression and calculation of the critical values
        - critical values (dict) – Critical values for the test statistic at the 1 %, 5 %, and 10 % levels. Based on MacKinnon (2010)
        - icbest (float) – The maximized information criterion if autolag is not None.
        - resstore (ResultStore, optional) – A dummy class with results attached as attributes


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

    ut = calcNotes(l1, l2)

    return adf(ut, maxlag = maxlag, regression = regression, autolag = autolag, store = store, regresults = regresults)
