#Prueba detección de colores zed
import rclpy
from std_msgs.msg import String
import imutils
import cv2
import numpy as np

def color_detection_node():
    rclpy.init()
    node = rclpy.create_node('color_detection_node')
    publisher = node.create_publisher(String, 'color_detected', 10)
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Definir rangos de colores
        yellow_osc = np.array([25, 70, 120])
        yellow_cla = np.array([30, 255, 255])

        red_osc = np.array([0, 50, 120])
        red_cla = np.array([10, 255, 255])

        green_osc = np.array([40, 70, 80])
        green_cla = np.array([70, 255, 255])

        blue_osc = np.array([90, 60, 0])
        blue_cla = np.array([121, 255, 255])

        cara1 = cv2.inRange(hsv, yellow_osc, yellow_cla)
        cara2 = cv2.inRange(hsv, red_osc, red_cla)
        cara3 = cv2.inRange(hsv, green_osc, green_cla)
        cara4 = cv2.inRange(hsv, blue_osc, blue_cla)

        cnts1 = cv2.findContours(cara1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts1 = imutils.grab_contours(cnts1)

        cnts2 = cv2.findContours(cara2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts2 = imutils.grab_contours(cnts2)

        cnts3 = cv2.findContours(cara3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts3 = imutils.grab_contours(cnts3)

        cnts4 = cv2.findContours(cara4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts4 = imutils.grab_contours(cnts4)

        for c in cnts1:
            area1 = cv2.contourArea(c)
            if area1 > 5000:
                cv2.drawContours(frame, [c], -1, (30, 255, 255), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "YELLOW", (cx - 20, cy - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
                print("Color detection: yellow")

                # Publicar el mensaje
                color_detected_msg = String()
                color_detected_msg.data = "yellow"
                publisher.publish(color_detected_msg)

        for c in cnts2:
            area2 = cv2.contourArea(c)
            if area2 > 5000:
                cv2.drawContours(frame, [c], -1, (0, 0, 255), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "RED", (cx - 20, cy - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
                print("Color detection: red")

                # Publicar el mensaje
                color_detected_msg = String()
                color_detected_msg.data = "red"
                publisher.publish(color_detected_msg)

        for c in cnts3:
            area3 = cv2.contourArea(c)
            if area3 > 5000:
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "GREEN", (cx - 20, cy - 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                print("Color detection: green")

                # Publicar el mensaje
                color_detected_msg = String()
                color_detected_msg.data = "green"
                publisher.publish(color_detected_msg)

        for c in cnts4:
            area4 = cv2.contourArea(c)
            if area4 > 5000:
                cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, "BLUE", (cx - 20, cy - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
                print("Color detection: blue")

                # Publicar el mensaje
                color_detected_msg = String()
                color_detected_msg.data = "blue"
                publisher.publish(color_detected_msg)

        cv2.imshow('Video', frame)
        k = cv2.waitKey(1)
        if k == 32:  # espacio
            break

if __name__ == '__main__':
    color_detection_node()
