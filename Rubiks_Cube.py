from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define los puntos del cubo
x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# Grafica los puntos del cubo
ax.scatter(x, y, z)
# Conecta los puntos para formar las caras del cubo
verts = [(0,1,2,3), (4,5,6,7), (0,4,7,3), (1,5,6,2), (0,1,5,4), (3,2,6,7)]
cube = Poly3DCollection([[(x[i], y[i], z[i]) for i in face] for face in verts], alpha=0.25)
ax.add_collection3d(cube)

# Establece los límites de los ejes
ax.set_xlim([0,1])
ax.set_ylim([0,1])
ax.set_zlim([0,1])

def update_view(elev, azim):
    ax.view_init(elev=elev, azim=azim)
    fig.canvas.draw()

# Conexión de los eventos del mouse a la función de actualización de la vista
def on_mouse_move(event):
    if event.button == 'left':
        elev, azim = ax.elev, ax.azim
        ax.elev = elev + (event.ydata - event.last_ydata)
        ax.azim = azim - (event.xdata - event.last_xdata)
        update_view(ax.elev, ax.azim)

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)

# Configuración de la ventana interactiva
plt.show(block=False)

# Bucle de la ventana interactiva
while plt.fignum_exists(fig.number):
    plt.pause(0.1)
