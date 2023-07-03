import cv2
import numpy as np

def filtro_sobel(imagem):
    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar o filtro Sobel nas direções x e y
    gradiente_x = cv2.Sobel(imagem_cinza, cv2.CV_64F, 1, 0, ksize=3)
    gradiente_y = cv2.Sobel(imagem_cinza, cv2.CV_64F, 0, 1, ksize=3)

    # Calcular a magnitude do gradiente
    magnitude = np.sqrt(np.square(gradiente_x) + np.square(gradiente_y))

    # Normalizar a magnitude para o intervalo [0, 255]
    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return magnitude

# Carregar a imagem
imagem = cv2.imread('C:/Users/User/Downloads/Original.jpg')

# Aplicar o filtro Sobel
imagem_filtrada = filtro_sobel(imagem)

# Exibir a imagem original e a imagem filtrada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Filtrada (Sobel)', imagem_filtrada)
cv2.waitKey(0)
cv2.destroyAllWindows()