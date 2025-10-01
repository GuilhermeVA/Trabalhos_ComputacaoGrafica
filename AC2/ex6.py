import matplotlib.pyplot as plt

P_x, P_y = 2, 5
P_label = 'P(2, 5)'


P_prime_x = -P_x
P_prime_y = P_y
P_prime_label = "P'(-2, 5)"




fig, ax = plt.subplots(figsize=(8, 6))


limite_x = max(abs(P_x), abs(P_prime_x)) + 1
limite_y = max(abs(P_y), abs(P_prime_y)) + 1
ax.set_xlim(-limite_x, limite_x)
ax.set_ylim(-1, limite_y)


ax.plot(P_x, P_y, 'o', color='blue', label='Ponto Original P')
ax.text(P_x + 0.1, P_y, P_label, fontsize=12, color='blue')

ax.plot(P_prime_x, P_prime_y, 's', color='red', label="Ponto Refletido P'")
ax.text(P_prime_x - 1.2, P_prime_y, P_prime_label, fontsize=12, color='red')


ax.axvline(x=0, color='gray', linestyle='--', linewidth=1.5, label='Eixo Y (Linho de Reflexão)')


ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)


ax.set_title('Reflexão do Ponto P(2, 5) em Relação ao Eixo Y')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_aspect('equal', adjustable='box') 
ax.legend()

plt.show()