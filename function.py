"""
import numpy as np
import matplot.pyplot as plt
x = np.arange(0.4*np.pi,0.01)
y = np.sin(x)
plt.plot(x,y)
plt.show()
"""

milo = ('milo', 100)
zou = ('zou', 6)
qi = ('qi', 99)

print("#    name:%-10shp:%6d" % milo)
print("#                   hp:%6d" % 100)
print("#    name:%-10shp:%6d" % qi)