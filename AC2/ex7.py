import matplotlib.pyplot as plt
import numpy as np


A = (2, 3)
B = (4, 3)
C = (3, 5)


original_x = [A[0], B[0], C[0], A[0]] 
original_y = [A[1], B[1], C[1], A[1]]


A_prime = (A[0], -A[1])
B_prime = (B[0], -B[1])
C_prime = (C[0], -C[1])

reflected_x = [A_prime[0], B_prime[0], C_prime[0], A_prime[0]]
reflected_y = [A_prime[1], B_prime[1], C_prime[1], A_prime[1]]



fig, ax = plt.subplots(figsize=(8, 6))


ax.plot(original_x, original_y, 'b-', label='Triângulo Original ABC')
ax.fill(original_x, original_y, 'b', alpha=0.3)
ax.text(A[0], A[1] + 0.1, f'A{A}', fontsize=12, color='darkblue')
ax.text(B[0], B[1] + 0.1, f'B{B}', fontsize=12, color='darkblue')
ax.text(C[0], C[1] + 0.1, f'C{C}', fontsize=12, color='darkblue')


ax.plot(reflected_x, reflected_y, 'r--', label="Triângulo Refletido A'B'C'")
ax.fill(reflected_x, reflected_y, 'r', alpha=0.3)
ax.text(A_prime[0], A_prime[1] - 0.3, f"A'{A_prime}", fontsize=12, color='darkred')
ax.text(B_prime[0], B_prime[1] - 0.3, f"B'{B_prime}", fontsize=12, color='darkred')
ax.text(C_prime[0], C_prime[1] - 0.3, f"C'{C_prime}", fontsize=12, color='darkred')


ax.axhline(y=0, color='gray', linestyle='-', linewidth=2, label='Eixo X (Linha de Reflexão)')


ax.axvline(x=0, color='black', linewidth=0.5)


max_coord = max(abs(np.array([original_x, original_y, reflected_x, reflected_y]).flatten())) + 1
ax.set_xlim(-1, max_coord)
ax.set_ylim(-max_coord, max_coord)

ax.set_title('Reflexão do Triângulo em Relação ao Eixo X')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_aspect('equal', adjustable='box') 

plt.show()

print(f"Novas Coordenadas dos Vértices:")
print(f"A' = {A_prime}")
print(f"B' = {B_prime}")
print(f"C' = {C_prime}")
