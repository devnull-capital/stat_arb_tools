from typing import Tuple

def calcOptimalStopLoss(M: float, gain: float, loss: float, chanceCorrect: float) -> float:
    """Calculates the optimal stop loss amount.


    Parameters
    ----------
    M : float
        The larges OL (Open minus Low) or HO (Hight minus Open) in the history of the data.
    gain : float
        The average gain of the historical plays that ended in a gain.
    loss : float
        The average loss of the historical plays that ended in a loss.
    chanceCorrect : float
        The percent of historical plays that ended in a gain.


    Returns
    -------
    float
        Returns the stop loss at which to close the play.


    """
    return 0.5 * (M + (1.0 - chanceCorrect) * loss - chanceCorrect * gain)

def calcOptimalVarStopLoss(b: float, vol: float, entry: float) -> Tuple[float, float]:
    """Calculates the optimal stop loss amount using the value at risk approach.


    Parameters
    ----------
    b : float
        The volatility multiplier.
    vol : float
        Historical volatility.
    entry : float
        The entry price


    Returns
    -------
    tuple of float
        Returns the stop loss at which to close the play using the value at risk approach for both short and long first.


    """
    return ((1 - b * vol) * entry, (1 + b * vol) * entry)

