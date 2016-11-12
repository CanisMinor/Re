import numpy as np
import math

def MeanSquaredError(actual, prediction):
    if len(actual) != len(prediction):
        return math.inf

    MAE = 0.0
    NumSamples = len(actual)
    for a, p in zip(actual, prediction):
        MAE = MAE + np.abs(actual-prediction)

    MAE = MAE / float(NumSamples)

    return MAE