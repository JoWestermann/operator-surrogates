import numpy as np


def l2_rel(true, pred, axis=-1, per_sample=False):
    error = np.sum((true - pred)**2, axis=axis)
    norm  = np.sum(true**2, axis=axis)
    if per_sample:
        return np.sqrt(error / norm)
    return np.sqrt(error.mean() / norm.mean())
