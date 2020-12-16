import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data_common"):
    os.makedirs("data_common")
    os.makedirs("data_common/train")
    os.makedirs("data_common/test")
    
    os.makedirs("data_common/train/0")
    os.makedirs("data_common/train/A")
    os.makedirs("data_common/train/B")
    os.makedirs("data_common/train/C")
    os.makedirs("data_common/train/D")
    os.makedirs("data_common/train/E")
    os.makedirs("data_common/train/F")
    os.makedirs("data_common/train/G")
    os.makedirs("data_common/train/H")
    os.makedirs("data_common/train/I")
    os.makedirs("data_common/train/J")
    
    
    os.makedirs("data_common/test/0")
    os.makedirs("data_common/test/A")
    os.makedirs("data_common/test/B")
    os.makedirs("data_common/test/C")
    os.makedirs("data_common/test/D")
    os.makedirs("data_common/test/E")
    os.makedirs("data_common/test/F")
    os.makedirs("data_common/test/G")
    os.makedirs("data_common/test/H")
    os.makedirs("data_common/test/I")
    os.makedirs("data_common/test/J")
       

# Train or test 
mode = 'train'
directory = 'data_common/'+mode+'/'

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'0': len(os.listdir(directory+"/0")),
             'A': len(os.listdir(directory+"/A")),
             'B': len(os.listdir(directory+"/B")),
             'C': len(os.listdir(directory+"/C")),
             'D': len(os.listdir(directory+"/D")),
             'E': len(os.listdir(directory+"/E")),
             'F': len(os.listdir(directory+"/F")),
             'G': len(os.listdir(directory+"/G")),
             'H': len(os.listdir(directory+"/H")),
             'I': len(os.listdir(directory+"/I")),
             'J': len(os.listdir(directory+"/J")),
             
             
             }
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "A-Empty : "+str(count['0']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "B-ILoveYou : "+str(count['A']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "C-Hii : "+str(count['B']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "D-Small : "+str(count['C']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "E-Love : "+str(count['D']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "F-Nice! : "+str(count['E']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "G-AllTheBest : "+str(count['F']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "H-Stop : "+str(count['G']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "I-Nope : "+str(count['H']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "J-CallMe : "+str(count['I']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "K-Bye : "+str(count['J']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)


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
    if interrupt & 0xFF == ord('A'):
        cv2.imwrite(directory+'A/'+str(count['A'])+'.jpg', roi)
    if interrupt & 0xFF == ord('B'):
        cv2.imwrite(directory+'B/'+str(count['B'])+'.jpg', roi)
    if interrupt & 0xFF == ord('C'):
        cv2.imwrite(directory+'C/'+str(count['C'])+'.jpg', roi)
    if interrupt & 0xFF == ord('D'):
        cv2.imwrite(directory+'D/'+str(count['D'])+'.jpg', roi)
    if interrupt & 0xFF == ord('E'):
        cv2.imwrite(directory+'E/'+str(count['E'])+'.jpg', roi)
    if interrupt & 0xFF == ord('F'):
        cv2.imwrite(directory+'F/'+str(count['F'])+'.jpg', roi)
    if interrupt & 0xFF == ord('G'):
        cv2.imwrite(directory+'G/'+str(count['G'])+'.jpg', roi)
    if interrupt & 0xFF == ord('H'):
        cv2.imwrite(directory+'H/'+str(count['H'])+'.jpg', roi)    
    if interrupt & 0xFF == ord('I'):
        cv2.imwrite(directory+'I/'+str(count['I'])+'.jpg', roi) 
    if interrupt & 0xFF == ord('J'):
        cv2.imwrite(directory+'J/'+str(count['J'])+'.jpg', roi)    
           
        
    
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
