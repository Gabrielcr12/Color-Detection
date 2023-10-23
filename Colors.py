import numpy as np
import cv2

# -----------------------Funcion por si no se detecta nada --------------------
def nada(x):
    pass

# ------------------------Creamos los sliders para detectar diferentes colores -----
cv2.namedWindow('Parametros')
cv2.createTrackbar('Tonalidad Minima', 'Parametros', 0, 179, nada)
cv2.createTrackbar('Tonalidad Maxima', 'Parametros', 0, 179, nada)  # Parametro H
cv2.createTrackbar('Pureza Minima', 'Parametros', 0, 255, nada)
cv2.createTrackbar('Pureza Maxima', 'Parametros', 0, 255, nada)  # Parametro S
cv2.createTrackbar('Luminosidad Minima', 'Parametros', 0, 255, nada)
cv2.createTrackbar('Luminosidad Maxima', 'Parametros', 0, 255, nada)  # Parametro V
cv2.createTrackbar('Kernel X', 'Parametros', 1, 30, nada)
cv2.createTrackbar('Kernel Y', 'Parametros', 1, 30, nada)  # Filtro

# ---------------------------- Crear el video ------------------------------------------
cap = cv2.VideoCapture(0)

while (1):
    # Capturamos la imagen de la cámara
    ret, frame = cap.read()
    # Si la imagen se capturó correctamente, procedemos
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos la imagen de RGB a HSV

        # Leemos los sliders
        Tmin = cv2.getTrackbarPos('Tonalidad Minima', 'Parametros')
        Tmax = cv2.getTrackbarPos('Tonalidad Maxima', 'Parametros')
        Pmin = cv2.getTrackbarPos('Pureza Minima', 'Parametros')
        Pmax = cv2.getTrackbarPos('Pureza Maxima', 'Parametros')
        Lmin = cv2.getTrackbarPos('Luminosidad Minima', 'Parametros')
        Lmax = cv2.getTrackbarPos('Luminosidad Maxima', 'Parametros')

        # Establecemos el rango mínimo y máximo para la codificación HSV
        color_oscuro = np.array([Tmin, Pmin, Lmin])
        color_brilla = np.array([Tmax, Pmax, Lmax])

        # Detectamos los píxeles que estén en el centro de los rangos
        mascara = cv2.inRange(hsv, color_oscuro, color_brilla)

        # Leemos los sliders que definen las dimensiones del kernel
        kernelx = cv2.getTrackbarPos('Kernel X', 'Parametros')
        kernely = cv2.getTrackbarPos('Kernel Y', 'Parametros')

        # Creamos el kernel para eliminar el ruido
        kernel = np.ones((kernelx, kernely), np.uint8)  # Creamos las dimensiones del filtro con una matriz
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)

        # Dibujar el rectángulo de donde está el color
        # Calcular los contornos guardándolos sin jerarquía, no es necesario
        # APPROX_SIMPLE es el método de aproximación de contorno, eliminando píxeles redundantes
        contornos, _ = cv2.findContours(mascara, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contornos, -1, (0, 0, 0), 2)

        # Mostramos la imagen de la cámara y la máscara
        cv2.imshow("camara", frame)
        cv2.imshow("Mascara", mascara)

        k = cv2.waitKey(1000)  # Espera 1 segundo
        if k == 27:
            cv2.destroyAllWindows()
            break

cap.release()
