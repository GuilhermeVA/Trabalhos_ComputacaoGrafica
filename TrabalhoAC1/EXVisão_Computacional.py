import cv2
import easyocr

# Inicializa o leitor (em português e inglês, pode adicionar 'pt' se quiser)
reader = easyocr.Reader(['en'])

# Carregar a imagem do carro
img_path = "imagens/carro.jpg"
img = cv2.imread(img_path)

# Reconhecimento de texto diretamente na imagem
results = reader.readtext(img_path)

for (bbox, text, prob) in results:
    print(f"Texto detectado: {text} (confiança: {prob:.2f})")

    # Desenhar caixa na imagem
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))

    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(img, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Mostrar resultado
cv2.imshow("Placa reconhecida", img)
cv2.waitKey(0)
cv2.destroyAllWindows()