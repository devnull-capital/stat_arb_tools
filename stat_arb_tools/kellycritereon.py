DivisionByZeroException = Exception("division by zero")
InvalidLossRatioException = Exception("invalid loss ratio")

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

def calcSimpKellyCritereon(p: float, r: float) -> float:
    """Calculates the simplified kelly critereon, which can be interpreted to be the fraction of the portfolio that you can afford to lose.


    Parameters
    ----------
    p : float
        The percent of times that a play results in a win.
    r : float
        The ratio of average loss to average gain.


    Returns
    -------
    float
        The percent of your portfolio that you can afford to lose.


    Raises
    ------
    InvalidLossRatioException
        The loss ratio must be less than one and greater than zero

    """
    if r > 1 or r < 0:
        raise InvalidLossRatioException

    return p - (1.0 - p) * r
