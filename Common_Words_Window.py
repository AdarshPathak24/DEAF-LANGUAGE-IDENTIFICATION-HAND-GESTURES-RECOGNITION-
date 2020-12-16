

from tkinter import *
from PIL import Image,ImageTk
import tkinter.font as font
import os

root=Tk()
root.title("Hand Gesture Recognition")
root.geometry('750x432')

labelFont=font.Font(size=20)

load = ImageTk.PhotoImage(Image.open("C:\\Users\\ADARSH PATHAK\\Desktop\\full project\\Colab\\Deaf-students-cover1.jpg"))
#load=Image.open('C:\\Users\\ANSHUL VERMA\\Desktop\\Project\\Hand_Gesture_Recognition\\Number_Recognition\\Deaf-students-cover1.jpg')
render=load
img=Label(root,image= render)
img.place(x=0,y=0)

#label= Label(root,text="Hand Gestures Recognition",width=100,height=10)
#label.place(x=0,y=0)
#label['font']=labelFont

def run1():
    print("Predict Common Words called")
    os.system('python predict_common.py')
    
def run2():
    print("Collect data called")
    os.system('python collect-data_common.py')
    
def run3():
    print("Train Common Words called")
    os.system('python train_common.py')    



B1= Button(root, text ="Predict Common Words",bg="black",fg="white",width=20,height=2,command = run1)
B1.place(relx=0,x=100,y=380,anchor=CENTER)

B2= Button(root, text ="Collect Data",bg="black",fg="white",width=20,height=2,command = run2)
B2.place(relx=0,x=360,y=380,anchor=CENTER)

B3= Button(root, text ="Train Your Model",bg="black",fg="white",width=20,height=2,command = run3)
B3.place(relx=0,x=620,y=380,anchor=CENTER)


#load2 = ImageTk.PhotoImage(Image.open("C:\\Users\\ANSHUL VERMA\\Desktop\\Project\\Hand_Gesture_Recognition\\Number_Recognition\\Text.jpg"))
#l1=Label(root,image=load2)
#l1.place(x=25,y=30)

label= Label(root,text="Common Words Prediction",width=23,height=1)
label.place(x=200,y=40)
label['font']=labelFont


root.mainloop()
