from .exceptions import ZeroHedgeRatioException

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
