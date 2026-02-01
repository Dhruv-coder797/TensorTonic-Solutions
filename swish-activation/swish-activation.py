import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
   
    s=(1.0/(1.0+np.exp(-x)))
    y=x*s
    if y.ndim==0:
        return y.reshape(1)
    return y
    