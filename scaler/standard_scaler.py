import numpy as np

class MyStandardScaler :

    def __init__(self):
        self.mean_ = None
        self.std_ = None

    def fit(self,X):
        X = np.array(X)
        self.mean_ = X.mean(axis=0)
        self.std_ = X.std(axis=0)
        return self
    
    def transform(self,X):

        X = np.array(X)
        if self.mean_ is None or self.std_ is None:
            raise Exception("please call fit() function before calling transform() function")
        return (X - self.mean_ ) / self.std_
    

    def fit_transform(self, X):
       
        return self.fit(X).transform(X)