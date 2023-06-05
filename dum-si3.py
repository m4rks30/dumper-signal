import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0, 10, 0.1)
y = np.sin(t)
plt.plot(t, y)
plt.title('Radio Frequencies')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
