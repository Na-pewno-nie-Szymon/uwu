import numpy as np

class Interpolacja:
    def __init__(self, data, linspace_x = 0) -> None:
        self.data = data
        self.lin_x = linspace_x
        self.h_i = self.h_and_b()['h']
        self.b_i = self.h_and_b()['b']
        self.u1 = 2*(self.h_i[0] + self.h_i[1])
        self.v1 = self.b_i[1] - self.b_i[0]
        self.n = data.shape[0] - 1

    def u_i(self):
        u_return = np.zeros(self.n - 1)
        u_return[0] = self.u1

        for i in range(1, self.n - 1):
            u_return[i] = 2*(self.h_i[i] + self.h_i[i+1]) - (self.h_i[i]**2)/u_return[i-1]

        return u_return
    
    def v_i(self):
        u_values = self.u_i()
        v_return = np.zeros(self.n - 1)
        v_return[0] = self.v1

        for i in range(1, self.n - 1):
            v_return[i] = self.b_i[i + 1] - self.b_i[i] - (self.h_i[i] * v_return[i-1])/u_values[i-1]

        return v_return

    def z_i(self):
        z_return = np.zeros(self.n + 1)
        v_values = self.v_i()
        u_values = self.u_i()

        for i in range(self.n - 1, 0, -1):
            z_return[i] = (v_values[i-1] - (self.h_i[i] * z_return[i+1]))/u_values[i-1]

        return z_return
    
    def h_and_b(self) -> dict:
        hb_return = {
            'h': np.zeros(self.data.shape[0] - 1),
            'b': np.zeros(self.data.shape[0] - 1)
        }

        for i in range(hb_return['h'].shape[0]):
            hb_return['h'][i] = self.data[i+1, 0] - self.data[i, 0]
            hb_return['b'][i] = (6/hb_return['h'][i]) * (self.data[i+1, 1] - self.data[i, 1])

        return hb_return

