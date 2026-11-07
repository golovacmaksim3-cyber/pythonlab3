import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Ellipse, Polygon, Rectangle

fig, ax = plt.subplots(figsize=(8, 8))

sky = Rectangle((0.0, 0.0), 8.0, 8.0, color='lightblue')
ax.add_patch(sky)

building = Rectangle((0.2, 0.1), 0.6, 0.7, color='lightslategrey')
ax.add_patch(building)

sun = Circle((0.924, 0.866), 0.08, color='gold')
ax.add_patch(sun)

cloud = Ellipse((0.25, 0.85), 0.25, 0.08, color='white')
ax.add_patch(cloud)

roof = Polygon([[0.15, 0.8], [0.5, 1.0], [0.85, 0.8]], color='firebrick')
ax.add_patch(roof)

door = Arc(
    (0.5, 0.1),
    0.2,
    0.3,
    angle=0,
    theta1=0,
    theta2=180,
    color='saddlebrown',
    linewidth=3,
)
ax.add_patch(door)

win1 = Rectangle((0.3, 0.5), 0.1, 0.15, color='lightyellow')
win2 = Rectangle((0.6, 0.5), 0.1, 0.15, color='lightyellow')
ground = Rectangle((0, 0), 1.0, 0.1, color='forestgreen')

ax.add_patch(win1)
ax.add_patch(win2)
ax.add_patch(ground)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.title('Городской пейзаж (Геометрические примитивы)')
plt.axis('off')


import os

os.makedirs('img', exist_ok=True)
plt.savefig('img/task3.png', bbox_inches='tight')
plt.show()
