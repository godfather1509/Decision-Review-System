from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import time, threading
import imutils

# Global variables for video and canvas dimensions
SET_WIDTH = 650
SET_HEIGHT = 358


# Function to update video frame on canvas
def update_frame():
    global cap, paused, frame1
    if not paused:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (SET_WIDTH, SET_HEIGHT))
            # resize the frame to adjust  in canvas
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # this converts color space of frame from (Blue,Green,Red) to (Red,Green,Blue)
            frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            canvas.create_image(0, 0, image=frame, anchor=NW)
            canvas.image = frame  # Keep a reference
            frame1 = cap.get(cv2.CAP_PROP_POS_FRAMES)

        else:
            cap.release()
            paused = True
    # Call update_frame after 15ms
    # frame has each of video frames stored in the form of matrices
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


# Function to update video playback speed (placeholder)
def play(speed):
    global cap, frame1
    print(f"Frame speed is {speed} frame")
    if cap.isOpened():
        cap.release()
    cap = cv2.VideoCapture(r"C:\Users\ayush\OneDrive\Desktop\multi mini project\DRS\cricket.mp4")
    # print(temp)
    # frame1 = temp
    frame1 = speed + frame1
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame1)
    grabbed, frame = cap.read()
    if not grabbed:
        canvas.create_text(120,25,fill="black",font="Times 26 bold",text="Clip Over")
        print("Clip Over")
        return
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0, 0, image=frame, anchor=NW)
    canvas.image = frame


# Function to pause the video
def pause():
    global paused
    paused = not paused
    # this inverts the value of paused in entire program stopping the update_frame() function instantaneously
    if paused:
        print("Video Paused")
    else:
        print("Video Resumed")
        update_frame()
        # this call of update_frame() begins the execution of program right from where it was paused


# Main Tkinter window setup
window = Tk()
window.title("Decision Review System")
global temp
temp = 0.0

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

btn6 = Button(window, text="<<Backwards(1 frame)", width=50, command=partial(play, -1))
btn6.pack()

btn2 = Button(window, text="Fast Forward >>", width=50, command=partial(play, 25))
btn2.pack()

btn7 = Button(window, text="Forward(1 frame)>>", width=50, command=partial(play, 1))
btn7.pack()

btn3 = Button(window, text="Pause", width=50, command=pause)
btn3.pack()

btn4 = Button(window, text="OUT", width=50, command=out)
btn4.pack()

btn5 = Button(window, text="NOT OUT", width=50, command=not_out)
btn5.pack()

# Start the Tkinter main loop
window.mainloop()
