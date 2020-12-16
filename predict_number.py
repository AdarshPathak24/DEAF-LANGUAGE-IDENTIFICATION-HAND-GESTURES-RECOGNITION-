import numpy as np
from tensorflow.keras.models import model_from_json
import operator
import cv2
import sys
import os

# Loading the model
json_file_number = open("model-bw_number.json", "r")
model_json_number = json_file_number.read()
json_file_number.close()
loaded_model = model_from_json(model_json_number)
# load weights into new model
loaded_model.load_weights("model-bw_number.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)

# Category dictionary
categories = {'0': 0, '1': '1', '2': '2', '3': '3', '4': '4', '5': '5' ,'6': '6', '7': '7', '8': '8', '9': '9', 'PYH': 'PYH'}

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)

    # Got this from collect-data.py
    # Coordinates of the ROI
    x1 = int(0.5 * frame.shape[1])
    y1 = 10
    x2 = frame.shape[1] - 10
    y2 = int(0.5 * frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0), 1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]

    # Resizing the ROI so it can be fed to the model for prediction
    roi = cv2.resize(roi, (96, 96))
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)
    # Batch of 1
    result = loaded_model.predict(test_image.reshape(1, 96, 96, 1))
    prediction = {'ZERO': result[0][0],
                  'ONE': result[0][1],
                  'TWO': result[0][2],
                  'THREE': result[0][3],
                  'FOUR': result[0][4],
                  'FIVE': result[0][5],
                  'SIX': result[0][6],
                  'SEVEN': result[0][7],
                  'EIGHT': result[0][8],
                  'NINE': result[0][9],
                  'PUT YOUR HAND': result[0][10],
                 }
    # Sorting based on top prediction
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)

    # Displaying the predictions
    cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 1)
    cv2.imshow("Frame", frame)

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27:  # esc key
        break

cap.release()
cv2.destroyAllWindows()
