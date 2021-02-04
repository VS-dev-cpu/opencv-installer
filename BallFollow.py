import serial

try:
  ser = serial.Serial('/dev/ttyACM0', 9600)
except:
  ser = serial.Serial('/dev/ttyACM1', 9600)

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 320)
_, frame = cap.read()
rows, cols, _ = frame.shape

ballX = 0
ballY = 0
ballSize = 0
ballDist = 0

debugging = False

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

    ballX = int(480 / 2)
    ballY = int(640 / 2)
    ballSize = 0
    ballDist = 0

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        
        ballX = int((x + x + w) / 2)
        ballY = int((y + y + h) / 2)
        ballSize = int((w + h) / 2)
        ballDist = int((ballY + (abs(ballSize) / 2)) / 2)
        if (debugging):
          print(str(ballX) + ', ' + str(ballY) + ', ' + 
          str(ballSize) + ', ' + str(ballDist) + '\n')
        break

    ser.write(bytes(str(ballX), 'utf-8') + b',' + bytes(str(ballY), 'utf-8') + b',')
    ser.write(bytes(str(ballSize), 'utf-8') + b',' + bytes(str(ballDist), 'utf-8'))
    ser.write(b'\n')
    
    if(debugging):
      cv2.line(frame, (ballX, 0), (ballX, 480), (0, 255, 0), 2)
      cv2.line(frame, (0, ballY), (640, ballY), (0, 255, 0), 2)
    
      cv2.imshow("Frame", frame)
      
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
