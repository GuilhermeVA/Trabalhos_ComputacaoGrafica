import matplotlib.pyplot as plt
import math


A = (1, 1)
B = (1, 4)
C = (4, 4)
D = (4, 1)
vertices = [A, B, C, D, A]


theta = math.radians(-45)


def rotate(p, theta):
    x, y = p
    x_rot = x * math.cos(theta) - y * math.sin(theta)
    y_rot = x * math.sin(theta) + y * math.cos(theta)
    return (round(x_rot, 4), round(y_rot, 4))


rotated_vertices = [rotate(p, theta) for p in vertices]


x_orig, y_orig = zip(*vertices)
x_rot, y_rot = zip(*rotated_vertices)


plt.figure(figsize=(7,7))
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.plot(x_orig, y_orig, 'b--', label='Original')
plt.plot(x_rot, y_rot, 'r-', label='Rotacionado (45° horário)')


for (x, y), label in zip(vertices[:-1], ['A','B','C','D']):
    plt.scatter(x, y, color='blue')
    plt.text(x+0.1, y, label, color='blue')
for (x, y), label in zip(rotated_vertices[:-1], ["A'","B'","C'","D'"]):
    plt.scatter(x, y, color='red')
    plt.text(x+0.1, y, label, color='red')

plt.title('Rotação de 45° Horário em torno da Origem')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()


print("Novas coordenadas após rotação de 45° horário:")
for label, p in zip(['A\'','B\'','C\'','D\''], rotated_vertices[:-1]):
    print(f"{label} = {p}")