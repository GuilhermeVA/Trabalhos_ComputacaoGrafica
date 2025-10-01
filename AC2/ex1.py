import matplotlib.pyplot as plt

# Ponto original
P = (2, 3)

# Vetor de translação
v = (4, -2)

# Novo ponto após a translação
P_transladado = (P[0] + v[0], P[1] + v[1])

# Plotagem
plt.figure(figsize=(6, 6))
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)

# Pontos
plt.scatter(*P, color='blue', label=f'P {P}', zorder=3)
plt.scatter(*P_transladado, color='red', label=f"P' {P_transladado}", zorder=3)

# Vetor de translação (seta)
plt.arrow(P[0], P[1], v[0], v[1],
          head_width=0.1, head_length=0.1,
          fc='green', ec='green', zorder=2, label='Translação')

# Rótulos dos pontos
plt.text(P[0] + 0.1, P[1] + 0.1, 'P', color='blue', fontsize=12)
plt.text(P_transladado[0] + 0.1, P_transladado[1] + 0.1, "P'", color='red', fontsize=12)

# Detalhes do gráfico
plt.title('Translação de P(2,3) pelo vetor (4,-2)')
plt.xlim(0, 8)
plt.ylim(0, 5)
plt.grid(True)
plt.legend()
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.show()

# Respostas no terminal
print(f"Ponto original: {P}")
print(f"Vetor de translação: {v}")
print(f"Novo ponto P': {P_transladado}")

# Respostas
# Ponto original: (2, 3)
# Vetor de translação: (4, -2)
# Novo ponto P': (6, 1)
# Coordenadas alteradas: x: 2 → 6, y: 3 → 1
