import pandas as pd
import numpy as np
class DP:
    def __init__(self, filename):
        self.filename = filename

    def readcsv(self):
        data = pd.read_csv(self.filename)
        print(data.shape)

    def readxlsx(self):
        data = pd.read_excel(self.filename)
        data = data.iloc[5:, 2:]
        Amp_dB = np.array(data.iloc[:, 0::2], dtype=np.float)
        Amp = np.power(10, Amp_dB/20)
        Phase = np.array(data.iloc[:, 1::2], dtype=np.float)
        data = Amp * np.exp(1j*Phase/180*np.pi)
        print(data)
        print(data.dtype)
        return data
        # data = np.exp(Phase)
        # print(Amp)
        # print(data)
        # print(data.dtype)
    def fromexcel2csv(self):
        pass
