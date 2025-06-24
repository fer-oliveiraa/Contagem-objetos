import cv2
import numpy as np

# 1. Carregar a imagem
img = cv2.imread('images/seeds.png')
original = img.copy()  # Cópia para salvar a versão final
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Melhorar contraste com equalização de histograma
gray = cv2.equalizeHist(gray)

# 3. Binarizar com Otsu + inversão (objetos em branco)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 4. Remover pequenos ruídos (morfologia - abertura)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

# 5. Área segura dos objetos (sure foreground)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

# 6. Determinar região do fundo (sure background)
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 7. Área desconhecida (fundo - frente)
unknown = cv2.subtract(sure_bg, sure_fg)

# 8. Marcadores para Watershed
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1  # Garante que o fundo seja 1, não 0
markers[unknown == 255] = 0

# 9. Aplicar Watershed
markers = cv2.watershed(img, markers)

# 10. Contar e desenhar objetos
contagem = 0
for label in np.unique(markers):
    if label <= 1:  # Ignora fundo e borda
        continue

    mask = np.uint8(markers == label)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 80:  # Filtro contra pequenos ruídos
            contagem += 1
            cv2.drawContours(original, [cnt], -1, (0, 255, 0), 2)

# 11. Mostrar número total de objetos detectados na imagem
cv2.putText(original, f'Objetos detectados: {contagem}', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

# 12. Salvar a imagem final
cv2.imwrite('images/resultado_seeds.png', original)

# 13. Exibir resultados
cv2.imshow("Imagem Final", original)
cv2.waitKey(0)
cv2.destroyAllWindows()
