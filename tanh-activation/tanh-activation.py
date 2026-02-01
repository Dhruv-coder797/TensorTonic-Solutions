import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    y=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    if y.ndim == 0:
        return y.reshape(1)
    return y
    pass