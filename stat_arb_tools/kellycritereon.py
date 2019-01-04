DivisionByZeroException = Exception("division by zero")

def calcKellyCritereon(chanceOfWin: float, avgWin: float, avgLoss) -> float:
    """Calculates the percent of a portfolio to commit to a given play.


    Parameters
    ----------
    chanceOfWin : float
        The percent of times that a play results in a win.
    avgWin : float
        The average roi when the play wins.
    avgLoss : float
        The average roi when the play loses. This number should be positive (e.g. 0.1 for 10%).


    Returns
    -------
    float
        The percent of your portfolio to commit to a given play.


    Raises
    ------
    DivisionByZeroException
        The parameters provided would reult in a division by zero.

    """
    if avgWin == 0 or avgLoss == 0:
        raise DivisionByZeroException

    return chanceOfWin*(1.0/avgLoss) - (1.0-chanceOfWin)*(1.0/avgWin)
