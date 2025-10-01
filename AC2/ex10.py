import numpy as np
import matplotlib.pyplot as plt

vertices_P0 = np.array([
    [1, 5, 5, 1, 1],
    [1, 1, 3, 3, 1]
])


P0 = vertices_P0[:, :-1]
pontos_hist = {'P0': P0}


vetor_translacao = np.array([[-2], [3]])

P1 = P0 + vetor_translacao
pontos_hist['P1'] = P1


matriz_escala = np.array([
    [1.5, 0],
    [0, 0.5]
])

P2 = matriz_escala @ P1
pontos_hist['P2'] = P2


matriz_reflexao_y = np.array([
    [-1, 0],
    [0, 1]
])

P_final = matriz_reflexao_y @ P2
pontos_hist['P_final'] = P_final


A_final = P_final[:, 0]
B_final = P_final[:, 1]
C_final = P_final[:, 2]
D_final = P_final[:, 3]

print(f"Coordenadas do retângulo inicial (P0):")
print(f"A(1, 1), B(5, 1), C(5, 3), D(1, 3)\n")
print("Coordenadas dos vértices após as transformações:")
print(f"A': ({A_final[0]:.1f}, {A_final[1]:.1f})")
print(f"B': ({B_final[0]:.1f}, {B_final[1]:.1f})")
print(f"C': ({C_final[0]:.1f}, {C_final[1]:.1f})")
print(f"D': ({D_final[0]:.1f}, {D_final[1]:.1f})")



def plot_rectangle(ax, vertices, color, label, linestyle='-', alpha=1.0):
    x = np.append(vertices[0, :], vertices[0, 0])
    y = np.append(vertices[1, :], vertices[1, 0])
    ax.plot(x, y, color=color, linestyle=linestyle, alpha=alpha, label=label)
    ax.plot(vertices[0, :], vertices[1, :], 'o', color=color, markersize=5) 

fig, ax = plt.subplots(figsize=(10, 8))


plot_rectangle(ax, pontos_hist['P0'], 'blue', '1. P0 (Inicial)', linestyle='-')
plot_rectangle(ax, pontos_hist['P1'], 'orange', '2. P1 (Translação)', linestyle='--')
plot_rectangle(ax, pontos_hist['P2'], 'green', '3. P2 (Escala)', linestyle='dotted')
plot_rectangle(ax, pontos_hist['P_final'], 'red', "4. P' (Reflexão - Final)", linestyle='-')


all_x = np.concatenate([v[0, :] for v in pontos_hist.values()])
all_y = np.concatenate([v[1, :] for v in pontos_hist.values()])

min_x, max_x = all_x.min() - 1, all_x.max() + 1
min_y, max_y = all_y.min() - 1, all_y.max() + 1


lim_x = max(abs(min_x), abs(max_x), 1)
lim_y = max(abs(min_y), abs(max_y), 1)
lim = max(lim_x, lim_y) * 1.1

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.set_title('Sequência de Transformações Geométricas em um Retângulo')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.legend(loc='lower left')
ax.set_aspect('equal', adjustable='box')

plt.show()