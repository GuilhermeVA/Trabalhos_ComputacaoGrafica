import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Definição dos vértices da pirâmide (base quadrada + ápice)
V0 = (0, 0, 0)
V1 = (1, 0, 0)
V2 = (1, 1, 0)
V3 = (0, 1, 0)
APEX = (0.5, 0.5, 1)  # ponto do topo

# Faces: base e quatro laterais
faces = [
    [V0, V1, V2, V3],  # base
    [V0, V1, APEX],    # lado 1
    [V1, V2, APEX],    # lado 2
    [V2, V3, APEX],    # lado 3
    [V3, V0, APEX],    # lado 4
]

# Criar figura
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection="3d")

# Desenhar pirâmide
poly = Poly3DCollection(faces, linewidths=1, alpha=0.85)
ax.add_collection3d(poly)

# Ajustar proporções e limites
ax.set_box_aspect([1, 1, 1])  # aspecto igual
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Esconder eixos para ficar mais limpo
ax.axis("off")

# Mostrar a figura
plt.show()