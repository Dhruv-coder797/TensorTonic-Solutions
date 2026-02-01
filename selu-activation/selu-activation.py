import numpy as np
def selu(x):
    """
    Apply SELU activation to each element.
    """
    x=np.asarray(x,dtype=float)
    y=np.where(x>0,1.0507*x,1.0507*1.6733*(np.exp(x)-1))
    return y.tolist()

    # Write code here