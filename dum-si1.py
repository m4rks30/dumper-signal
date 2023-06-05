import numpy as np
signal = np.random.random(100)
dumped_signal = signal * 0.5
import matplotlib.pyplot as plt
plt.plot(signal, label="Original Signal")
plt.plot(dumped_signal, label="Dumped Signal")
plt.legend()
plt.show()
