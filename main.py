from readdata import DP
import numpy as np
from matplotlib import pyplot as plt
path = './data/Book1.xlsx'

dp = DP(path)
raw_data = np.transpose(dp.readxlsx())
range_profile = np.fft.fft(raw_data, axis=0)
ISAR_imaging = np.fft.fftshift(np.fft.fft(range_profile, axis=1), axes=1)
dB_ISAR_imaging = 20 * np.log10(ISAR_imaging/np.max(ISAR_imaging))
plt.pcolor(np.abs(ISAR_imaging), cmap='jet')
plt.xlabel('Doppler Cell')
plt.ylabel('Range Cell')
plt.title('RD')
plt.show()
print("---------------------")


