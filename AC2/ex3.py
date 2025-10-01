import matplotlib.pyplot as plt


A = (1, 1)
B = (3, 1)
C = (2, 4)


kx = 2
ky = 0.5


A_esc = (A[0]*kx, A[1]*ky)
B_esc = (B[0]*kx, B[1]*ky)
C_esc = (C[0]*kx, C[1]*ky)


x_original = [A[0], B[0], C[0], A[0]]
y_original = [A[1], B[1], C[1], A[1]]

x_escalado = [A_esc[0], B_esc[0], C_esc[0], A_esc[0]]
y_escalado = [A_esc[1], B_esc[1], C_esc[1], A_esc[1]]


plt.figure(figsize=(7,7))
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)


plt.plot(x_original, y_original, 'b--', label='Triângulo original')
plt.plot(x_escalado, y_escalado, 'r-', label='Triângulo escalado (kx=2, ky=0.5)')


plt.scatter(*A, color='blue')
plt.scatter(*B, color='blue')
plt.scatter(*C, color='blue')
plt.scatter(*A_esc, color='red')
plt.scatter(*B_esc, color='red')
plt.scatter(*C_esc, color='red')


plt.text(A[0]+0.1, A[1], 'A', color='blue')
plt.text(B[0]+0.1, B[1], 'B', color='blue')
plt.text(C[0]+0.1, C[1], 'C', color='blue')
plt.text(A_esc[0]+0.1, A_esc[1], "A'", color='red')
plt.text(B_esc[0]+0.1, B_esc[1], "B'", color='red')
plt.text(C_esc[0]+0.1, C_esc[1], "C'", color='red')


plt.grid(True)
plt.legend()
plt.title('Escala não uniforme (kx=2, ky=0.5)')
plt.xlim(0, 8)
plt.ylim(0, 5)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.gca().set_aspect('equal', adjustable='box')

plt.show()


print("Novas coordenadas após escala não uniforme (kx=2, ky=0.5):")
print(f"A' = {A_esc}")
print(f"B' = {B_esc}")
print(f"C' = {C_esc}")
print("Área permanece igual (fator = kx * ky = 1).")