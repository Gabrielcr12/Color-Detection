# Detección de Colores con OpenCV
El codigo identifica tres colores principales a traves del uso de OpenCV y publica el color detectado.

## Funcionamiento

1. **Configuración de ROS 2**:
   - Inicializa ROS 2 con `rclpy.init()`.
   - Crea un nodo de ROS 2 llamado "color_detection_node" y un publicador para enviar mensajes de tipo `String` al tema "color_detected".

2. **Configuración de la Cámara**:
   - Abre la cámara con `cv2.VideoCapture(0)` (la cámara predeterminada).
   - Establece el tamaño del fotograma capturado con `cap.set(3, 640)` y `cap.set(4, 480)`.

3. **Bucle Principal**:
   - Comienza un bucle infinito para capturar video en tiempo real.

4. **Detección de Colores**:
   - Convierte cada fotograma al espacio de color HSV.
   - Define rangos de colores para amarillo, rojo, verde y azul en formato HSV.
   - Crea máscaras para aislar los píxeles dentro de los rangos de color especificados.
   - Encuentra contornos en las áreas coloreadas.

5. **Procesamiento de Contornos**:
   - Itera sobre los contornos de cada color.
   - Filtra el ruido basándose en el área del contorno (umbral de 5000 píxeles).
   - Dibuja los contornos en el video y marca el centro de masa.
   - Muestra el nombre del color detectado en el video.
   - Publica mensajes de tipo `String` en ROS 2 indicando el color detectado.

6. **Visualización en Tiempo Real**:
   - Muestra el video en tiempo real con los contornos y etiquetas de color superpuestos.

7. **Salida del Bucle y Finalización**:
   - El bucle se detiene al presionar la tecla de espacio (`k == 32`).
   - Libera los recursos de la cámara y cierra la ventana de video.

8. **Ejecución del Nodo**:
   - El código se ejecuta como un nodo ROS 2 llamado "color_detection_node". 
