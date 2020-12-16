import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data_number"):
    os.makedirs("data_number")
    os.makedirs("data_number/train")
    os.makedirs("data_number/test")
    
    os.makedirs("data_number/train/0")
    os.makedirs("data_number/train/1")
    os.makedirs("data_number/train/2")
    os.makedirs("data_number/train/3")
    os.makedirs("data_number/train/4")
    os.makedirs("data_number/train/5")
    os.makedirs("data_number/train/6")
    os.makedirs("data_number/train/7")
    os.makedirs("data_number/train/8")
    os.makedirs("data_number/train/9")
    os.makedirs("data_number/train/PYH")
    
    
    os.makedirs("data_number/test/0")
    os.makedirs("data_number/test/1")
    os.makedirs("data_number/test/2")
    os.makedirs("data_number/test/3")
    os.makedirs("data_number/test/4")
    os.makedirs("data_number/test/5")
    os.makedirs("data_number/test/6")
    os.makedirs("data_number/test/7")
    os.makedirs("data_number/test/8")
    os.makedirs("data_number/test/9")
    os.makedirs("data_number/test/PYH")
        

# Train or test 
mode = 'train'
directory = 'data_number/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'0': len(os.listdir(directory+"/0")),
             '1': len(os.listdir(directory+"/1")),
             '2': len(os.listdir(directory+"/2")),
             '3': len(os.listdir(directory+"/3")),
             '4': len(os.listdir(directory+"/4")),
             '5': len(os.listdir(directory+"/5")),
             '6': len(os.listdir(directory+"/6")),
             '7': len(os.listdir(directory+"/7")),
             '8': len(os.listdir(directory+"/8")),
             '9': len(os.listdir(directory+"/9")),
             'PYH': len(os.listdir(directory+"/PYH")),
                          
             }
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Zero : "+str(count['0']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "One : "+str(count['1']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Two : "+str(count['2']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Three : "+str(count['3']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Four : "+str(count['4']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Five : "+str(count['5']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Six : "+str(count['6']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Seven : "+str(count['7']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Eight : "+str(count['8']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Nine : "+str(count['9']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Empty : "+str(count['PYH']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
        
    
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (400, 400)) 
 
    cv2.imshow("Frame", frame)
    
    #_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(mask, kernel, iterations=1)
    #img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['0'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['1'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['2'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['3'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['4'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['5'])+'.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['6'])+'.jpg', roi)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['7'])+'.jpg', roi)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['8'])+'.jpg', roi)    
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(directory+'9/'+str(count['9'])+'.jpg', roi)
    if interrupt & 0xFF == ord('P'):
        cv2.imwrite(directory+'PYH/'+str(count['PYH'])+'.jpg', roi)    
        
    
cap.release()
cv2.destroyAllWindows()
"""
d = "old-data/test/0"
newd = "data/test/0"
for walk in os.walk(d):
    for file in walk[2]:
        roi = cv2.imread(d+"/"+file)
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(newd+"/"+file, mask)     
"""
