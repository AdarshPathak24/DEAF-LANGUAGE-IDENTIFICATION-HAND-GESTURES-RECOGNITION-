import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data_alphabet"):
    os.makedirs("data_alphabet")
    os.makedirs("data_alphabet/train")
    os.makedirs("data_alphabet/test")
    
    os.makedirs("data_alphabet/train/0")
    os.makedirs("data_alphabet/train/A")
    os.makedirs("data_alphabet/train/B")
    os.makedirs("data_alphabet/train/C")
    os.makedirs("data_alphabet/train/D")
    os.makedirs("data_alphabet/train/E")
    os.makedirs("data_alphabet/train/F")
    os.makedirs("data_alphabet/train/G")
    os.makedirs("data_alphabet/train/H")
    os.makedirs("data_alphabet/train/I")
    os.makedirs("data_alphabet/train/J")
    os.makedirs("data_alphabet/train/K")
    os.makedirs("data_alphabet/train/L")
    os.makedirs("data_alphabet/train/M")
    os.makedirs("data_alphabet/train/N")
    os.makedirs("data_alphabet/train/O")
    os.makedirs("data_alphabet/train/P")
    os.makedirs("data_alphabet/train/Q")
    os.makedirs("data_alphabet/train/R")
    os.makedirs("data_alphabet/train/S")
    os.makedirs("data_alphabet/train/T")
    os.makedirs("data_alphabet/train/U")
    os.makedirs("data_alphabet/train/V")
    os.makedirs("data_alphabet/train/W")
    os.makedirs("data_alphabet/train/X")
    os.makedirs("data_alphabet/train/Y")
    os.makedirs("data_alphabet/train/Z")
    
    os.makedirs("data_alphabet/test/0")
    os.makedirs("data_alphabet/test/A")
    os.makedirs("data_alphabet/test/B")
    os.makedirs("data_alphabet/test/C")
    os.makedirs("data_alphabet/test/D")
    os.makedirs("data_alphabet/test/E")
    os.makedirs("data_alphabet/test/F")
    os.makedirs("data_alphabet/test/G")
    os.makedirs("data_alphabet/test/H")
    os.makedirs("data_alphabet/test/I")
    os.makedirs("data_alphabet/test/J")
    os.makedirs("data_alphabet/test/K")
    os.makedirs("data_alphabet/test/L")
    os.makedirs("data_alphabet/test/M")
    os.makedirs("data_alphabet/test/N")
    os.makedirs("data_alphabet/test/O")
    os.makedirs("data_alphabet/test/P")
    os.makedirs("data_alphabet/test/Q")
    os.makedirs("data_alphabet/test/R")
    os.makedirs("data_alphabet/test/S")
    os.makedirs("data_alphabet/test/T")
    os.makedirs("data_alphabet/test/U")
    os.makedirs("data_alphabet/test/V")
    os.makedirs("data_alphabet/test/W")
    os.makedirs("data_alphabet/test/X")
    os.makedirs("data_alphabet/test/Y")
    os.makedirs("data_alphabet/test/Z")
    

# Train or test 
mode = 'train'
directory = 'data_alphabet/'+mode+'/'

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
             'K': len(os.listdir(directory+"/K")),
             'L': len(os.listdir(directory+"/L")),
             'M': len(os.listdir(directory+"/M")),
             'N': len(os.listdir(directory+"/N")),
             'O': len(os.listdir(directory+"/O")),
             'P': len(os.listdir(directory+"/P")),
             'Q': len(os.listdir(directory+"/Q")),
             'R': len(os.listdir(directory+"/R")),
             'S': len(os.listdir(directory+"/S")),
             'T': len(os.listdir(directory+"/T")),
             'U': len(os.listdir(directory+"/U")),
             'V': len(os.listdir(directory+"/V")),
             'W': len(os.listdir(directory+"/W")),
             'X': len(os.listdir(directory+"/X")),
             'Y': len(os.listdir(directory+"/Y")),
             'Z': len(os.listdir(directory+"/Z")),
             
             }
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "0 : "+str(count['0']), (80, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "A : "+str(count['A']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "B : "+str(count['B']), (10, 135), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "C : "+str(count['C']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "D : "+str(count['D']), (10, 165), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "E : "+str(count['E']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "F : "+str(count['F']), (10, 195), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "G : "+str(count['G']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "H : "+str(count['H']), (10, 225), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "I : "+str(count['I']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "J : "+str(count['J']), (10, 255), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "K : "+str(count['K']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "L : "+str(count['L']), (10, 285), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "M : "+str(count['M']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "N : "+str(count['N']), (10, 315), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "O : "+str(count['O']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "P : "+str(count['P']), (10, 345), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Q : "+str(count['Q']), (10, 360), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "R : "+str(count['R']), (10, 375), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "S : "+str(count['S']), (10, 390), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "T : "+str(count['T']), (10, 405), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "U : "+str(count['U']), (10, 420), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "V : "+str(count['V']), (10, 435), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "W : "+str(count['W']), (10, 450), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "X : "+str(count['X']), (10, 465), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Y : "+str(count['Y']), (80, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Z : "+str(count['Z']), (80, 135), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    
    
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
    if interrupt & 0xFF == ord('K'):
        cv2.imwrite(directory+'K/'+str(count['K'])+'.jpg', roi)    
    if interrupt & 0xFF == ord('L'):
        cv2.imwrite(directory+'L/'+str(count['L'])+'.jpg', roi)
    if interrupt & 0xFF == ord('M'):
        cv2.imwrite(directory+'M/'+str(count['M'])+'.jpg', roi)
    if interrupt & 0xFF == ord('N'):
        cv2.imwrite(directory+'N/'+str(count['N'])+'.jpg', roi)
    if interrupt & 0xFF == ord('O'):
        cv2.imwrite(directory+'O/'+str(count['O'])+'.jpg', roi)    
    if interrupt & 0xFF == ord('P'):
        cv2.imwrite(directory+'P/'+str(count['P'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Q'):
        cv2.imwrite(directory+'Q/'+str(count['Q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('R'):
        cv2.imwrite(directory+'R/'+str(count['R'])+'.jpg', roi)
    if interrupt & 0xFF == ord('S'):
        cv2.imwrite(directory+'S/'+str(count['S'])+'.jpg', roi)
    if interrupt & 0xFF == ord('T'):
        cv2.imwrite(directory+'T/'+str(count['T'])+'.jpg', roi)
    if interrupt & 0xFF == ord('U'):
        cv2.imwrite(directory+'U/'+str(count['U'])+'.jpg', roi)
    if interrupt & 0xFF == ord('V'):
        cv2.imwrite(directory+'V/'+str(count['V'])+'.jpg', roi)
    if interrupt & 0xFF == ord('W'):
        cv2.imwrite(directory+'W/'+str(count['W'])+'.jpg', roi)
    if interrupt & 0xFF == ord('X'):
        cv2.imwrite(directory+'X/'+str(count['X'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Y'):
        cv2.imwrite(directory+'Y/'+str(count['Y'])+'.jpg', roi)
    if interrupt & 0xFF == ord('Z'):
        cv2.imwrite(directory+'Z/'+str(count['Z'])+'.jpg', roi)
        
    
           
        
    
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
