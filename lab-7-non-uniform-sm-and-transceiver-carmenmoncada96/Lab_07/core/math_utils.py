import numpy as np

def linear_to_db(x):
    return 10*np.log10(x)

def db_to_linear(x):
    return 10**(x/10)