import matplotlib.pyplot as plt
import math


P = (1, 0)


theta = 90
rad = math.radians(theta)


x, y = P
x_rot = x * math.cos(rad) - y * math.sin(rad)
y_rot = x * math.sin(rad) + y * math.cos(rad)
P_rot = (round(x_rot, 2), round(y_rot, 2))


plt.figure(figsize=(6,6))
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)


plt.scatter(*P, color='blue', label=f'P {P}')
plt.scatter(*P_rot, color='red', label=f"P' {P_rot}")


plt.plot([0, P[0]], [0, P[1]], 'b--')
plt.plot([0, P_rot[0]], [0, P_rot[1]], 'r-')


plt.text(P[0]+0.05, P[1], 'P', color='blue')
plt.text(P_rot[0]+0.05, P_rot[1], "P'", color='red')


plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Rotação de 90° anti-horária em torno da origem')
plt.grid(True)
plt.legend()
plt.show()

print(f"Ponto original: {P}")
print(f"Ponto rotacionado (90° anti-horário): {P_rot}")