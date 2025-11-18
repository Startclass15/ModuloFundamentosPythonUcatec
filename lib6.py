#MAPAS DE CALOR (imshow()) =>colorbar
import matplotlib.pyplot as plt
import numpy as np

matriz=np.random.rand(5,5)

plt.imshow(matriz)
plt.colorbar()
plt.show()