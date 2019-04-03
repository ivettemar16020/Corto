import numpy as np

def derivative_j(theta, X, y): 
    m = len(y) #shape Xsubzero 
    hipo = X.dot(theta)
    for(i in range(m)):
        der = (1/m) * np.sum((hipo - y)*X[i])
          
    return der
