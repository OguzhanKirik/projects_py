import matplotlib.pyplot as plt

from random_wallk import RandomWalk

rw = RandomWalk(50000)

rw.fill_walk()

plt.style.use('classic')
#fig, ax =  plt.subplots()
#fig, ax = plt.subplots(figsize=(15, 9))
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
#ax.scatter(rw.x_values, rw.y_values, s=15)
# point_numbers = range(rw.num_points)
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
# edgecolors='none', s=15)

# Emphasize the first and last points.
# ax.scatter(0, 0, c='green', edgecolors='none', s=100)
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
# s=100)


ax.scatter(rw.x_values, rw.y_values, cmap=plt.cm.Blues,
edgecolor='none', s=1) 

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

