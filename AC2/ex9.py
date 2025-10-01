import numpy as np
import matplotlib.pyplot as plt


P = np.array([3, 2])
pontos = [P]


vetor_translacao = np.array([1, -1])
P1 = P + vetor_translacao
pontos.append(P1)


matriz_rotacao = np.array([[0, -1],
                           [1,  0]])

P2 = matriz_rotacao @ P1
pontos.append(P2)


fator_escala = 2

P_final = fator_escala * P2
pontos.append(P_final)

print(f"Ponto inicial P: {P}")
print(f"1. Após Translação (P1): {P1}")
print(f"2. Após Rotação (P2): {P2}")
print(f"3. Após Escala (P'): {P_final}")
print(f"\nA nova posição final do ponto P' é: {P_final}")



pontos_np = np.array(pontos)
x = pontos_np[:, 0]
y = pontos_np[:, 1]

plt.figure(figsize=(8, 8))
plt.plot(x, y, 'o', color='gray', linestyle='--', alpha=0.6, label='Caminho das Transformações')


plt.plot(x[0], y[0], 'o', color='blue', markersize=8, label=f'P inicial (3, 2)')
plt.plot(x[1], y[1], 's', color='orange', markersize=8, label=f'P1 Translação (4, 1)')
plt.plot(x[2], y[2], '^', color='green', markersize=8, label=f'P2 Rotação (-1, 4)')
plt.plot(x[3], y[3], 'D', color='red', markersize=10, label=f'P\' Final (-2, 8)')


plt.text(x[0], y[0] + 0.3, 'P(3, 2)', fontsize=9, ha='center')
plt.text(x[1], y[1] - 0.5, 'P1(4, 1)', fontsize=9, ha='center')
plt.text(x[2], y[2] - 0.5, 'P2(-1, 4)', fontsize=9, ha='center')
plt.text(x[3], y[3] + 0.3, 'P\'(-2, 8)', fontsize=10, ha='center', fontweight='bold')


max_val = max(np.abs(x.max()), np.abs(x.min()), np.abs(y.max()), np.abs(y.min())) + 1
limite = np.ceil(max_val / 2) * 2 
plt.xlim(-limite, limite)
plt.ylim(-limite, limite)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Transformações Geométricas Consecutivas')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend(loc='upper left')
plt.gca().set_aspect('equal', adjustable='box') 
plt.show()