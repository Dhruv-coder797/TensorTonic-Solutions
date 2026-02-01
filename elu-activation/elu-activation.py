import numpy as dhruv
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x=dhruv.asarray(x,dtype=float)
    y=dhruv.where(x>0,x,alpha*(dhruv.exp(x)-1))
    return y.tolist()
   