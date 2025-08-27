import cv2

# Carregar imagem
img = cv2.imread("imagens/Goldens.jpg")

# Aumentar contraste e brilho com a fórmula:
# nova_img = alpha * img + beta
alpha = 1.8  # fator de contraste (>1 aumenta, <1 reduz)
beta = 0     # brilho (0 mantém, positivo clareia)

contraste_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Mostrar resultado
cv2.imshow("Original", img)
cv2.imshow("Com mais contraste", contraste_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Salvar resultado
cv2.imwrite("imagem_contraste.jpg", contraste_img)