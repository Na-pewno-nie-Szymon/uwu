#sklej mi jaja
import numpy as np

class interpolacja_sklajnami:
    def __init__(self, data, linspace_start, linspace_end, linspace_limit) -> None:
        self.data  = data
        self.start = linspace_start
        self.end   = linspace_end
        self.limit = linspace_limit
        self.lin_x = np.linspace(linspace_start, linspace_end, linspace_limit)

    def a_i(self):
        a_return = np.zeros(self.data.shape[0])

        for i in range(self.data.shape[0] - 1):
            a_return[i] = (self.data[i+1, 1] - self.data[i, 1]) / (self.data[i+1, 0] - self.data[i, 0])
        
        return a_return

    def S_i(self):
        Si = np.zeros(self.lin_x.shape[0])
        for i in range(self.data.shape[0] - 1):
            Si += ((self.data[i+1, 1] - self.data[i, 1])/(self.data[i+1, 0] - self.data[i, 0]) * (self.lin_x - self.data[i, 0]) + self.data[i, 1]) * (self.lin_x < self.data[i+1, 0]) * (self.lin_x >= self.data[i, 0]) 
        
        return Si
