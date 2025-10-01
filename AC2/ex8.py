import matplotlib.pyplot as plt
import numpy as np


P_x, P_y = 2, 3
k = 2 



P_prime_x = P_x + k * P_y

P_prime_y = P_y

P_label = f'P({P_x}, {P_y})'
P_prime_label = f"P'({P_prime_x}, {P_prime_y})"



fig, ax = plt.subplots(figsize=(8, 6))


ax.plot(P_x, P_y, 'o', color='blue', label='Ponto Original P')
ax.text(P_x - 0.5, P_y - 0.4, P_label, fontsize=12, color='blue')


ax.plot(P_prime_x, P_prime_y, 's', color='red', label="Ponto Cisalhado P'")
ax.text(P_prime_x - 0.5, P_prime_y - 0.4, P_prime_label, fontsize=12, color='red')

ax.plot([P_x, P_prime_x], [P_y, P_prime_y], 'k:', alpha=0.6, label='Deslocamento Horizontal')

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)


max_val = max(P_prime_x, P_prime_y) + 1
min_val = min(0, P_y) - 1
ax.set_xlim(min_val, max_val)
ax.set_ylim(min_val, max_val)

ax.set_title(f'Cisalhamento Horizontal (k={k}) do Ponto P(2, 3)')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_aspect('equal', adjustable='box') 
ax.legend()

plt.show()