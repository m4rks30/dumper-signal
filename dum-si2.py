from sklearn import preprocessing
import numpy as np
signal = np.random.random(100)
scaler = preprocessing.MinMaxScaler(feature_range=(-1,1))
scaled_signal = scaler.fit_transform(signal.reshape(-1,1))
import matplotlib.pyplot as plt
plt.plot(signal, label="Original Signal")
plt.plot(scaled_signal, label="Dumped Signal")
plt.legend()
plt.show()
