from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import time, threading
import imutils

# Global variables for video and canvas dimensions
SET_WIDTH = 650
SET_HEIGHT = 358

# Initialize global variables
paused = False
cap = None
temp = 0.0

# Function to update video frame on canvas
def update_frame():
    global cap, paused
    if not paused:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (SET_WIDTH, SET_HEIGHT))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            canvas.create_image(0, 0, image=frame, anchor=NW)
            canvas.image = frame  # Keep a reference
        else:
            cap.release()
            paused = True
    if not paused:
        window.after(15, update_frame)

def pending(decision):
    global cap, paused
    path1 = r"C:\Users\ayush\OneDrive\Desktop\multi mini project\DRS\DP.mp4"
    if cap.isOpened():
        cap.release()
    cap = cv2.VideoCapture(path1)
    paused = False
    update_frame()
    time.sleep(6)
    if decision == "out":
        path1 = r"C:\Users\ayush\OneDrive\Desktop\multi mini project\DRS\OUT.mp4"
    elif decision == "not out":
        path1 = r"C:\Users\ayush\OneDrive\Desktop\multi mini project\DRS\NOT OUT.mp4"

    if cap.isOpened():
        cap.release()
    cap = cv2.VideoCapture(path1)
    paused = False
    update_frame()

def out():
    thre = threading.Thread(target=pending, args=("out",))
    thre.daemon = 1
    thre.start()
    print("Player is out")

def not_out():
    thre = threading.Thread(target=pending, args=("not out",))
    thre.daemon = 1
    thre.start()
    print("Player is Not out")

def play(speed):
    global cap, temp
    print(f"Frame speed is {speed} frame")
    if cap.isOpened():
        cap.release()
    cap = cv2.VideoCapture("Welcome.mp4")
    frame1 = cap.get(cv2.CAP_PROP_POS_FRAMES)
    print(temp)
    frame1 = temp
    print(frame1)
    a = speed + frame1
    cap.set(cv2.CAP_PROP_POS_FRAMES, a)
    temp = frame1 + speed
    print(temp)
    grabbed, frame = cap.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0, 0, image=frame, anchor=NW)
    canvas.image = frame

def pause():
    global paused
    paused = not paused
    if paused:
        print("Video Paused")
    else:
        print("Video Resumed")
        update_frame()

# Main Tkinter window setup
window = Tk()
window.title("Decision Review System")

# Create canvas to display video frames
canvas = Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
canvas.pack()

# Open video file
path_opening = r"C:\Users\ayush\OneDrive\Desktop\multi mini project\DRS\OPENING.mp4"
cap = cv2.VideoCapture(path_opening)
paused = False

# Initialize video frame update
update_frame()

# Buttons for video control
btn1 = Button(window, text="<<Fast Backwards", width=50, command=partial(play, -25))
btn1.pack()

btn6 = Button(window, text="<<Backwards(1 frame)", width=50, command=partial(play, -2))
btn6.pack()

btn2 = Button(window, text="Fast Forward >>", width=50, command=partial(play, 25))
btn2.pack()

btn7 = Button(window, text="Forward(1 frame)>>", width=50, command=partial(play, 2))
btn7.pack()

btn3 = Button(window, text="Pause", width=50, command=pause)
btn3.pack()

btn4 = Button(window, text="OUT", width=50, command=out)
btn4.pack()

btn5 = Button(window, text="NOT OUT", width=50, command=not_out)
btn5.pack()

# Start the Tkinter main loop
window.mainloop()
