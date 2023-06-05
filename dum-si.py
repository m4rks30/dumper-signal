import numpy as np
import matplotlib.pyplot as plt
freq = np.linspace(0, 1000, 1000)  
signal = np.random.rand(1000) 
plt.plot(freq, signal)
plt.xlabel('Frequency (MHz)')
plt.ylabel('Signal Strength')
plt.title('Radio Frequency Spectrum')
plt.show()
