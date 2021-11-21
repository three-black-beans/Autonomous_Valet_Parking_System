import numpy as np
import matplotlib.pyplot as plt

# matplotlib code practice
# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html

t = np.arange(0., 5., 0.2)
# evenly sampled time at 200ms intervals
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# red dashes, blue squares and green triangles
plt.savefig('example_images/example1.png')
plt.show()
