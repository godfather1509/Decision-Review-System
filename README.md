# Abstract
This publication presents the design and implementation of a Decision Review System (DRS) using **Python**, aimed at emulating the functionalities of professional cricket match review systems. The project leverages **Tkinter** to create an intuitive and user-friendly graphical interface, ensuring ease of use for operators. **OpenCV**, a powerful library for computer vision, is utilized for video analysis and processing, enabling real-time playback, frame-by-frame analysis, and annotation features. This system is designed to provide a robust platform for decision-making, focusing on accuracy and efficiency. The project’s practical application and testing demonstrate its potential to support critical decisions in cricket and similar sports.

# Methodology

## System Architecture:

The Decision Review System is composed of two main modules:

1. **User Interface Module**: Built with Tkinter, this module provides controls for video playback and frame navigation. The layout is optimized for ease of use and quick access to core functionalities.

2. **Video Processing Module**: Developed using OpenCV, this module handles the loading, analysis, and manipulation of video content. Features include real-time playback, slow motion, and frame-by-frame navigation, essential for scrutinizing pivotal moments in matches.

## Implementation Steps

#### Tkinter Interface Design:

- A responsive window layout featuring buttons, sliders, and a video display area.

- Navigation controls to pause, play, and step through video frames.

```python
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
```

![Screenshot 2024-12-30 172724.png](Screenshot%202024-12-30%20172724.png)

#### Video Handling with OpenCV:

- Integration of OpenCV to support various video formats and frame extraction.

- Implementation of playback controls and real-time processing pipelines.

```python
def update_frame():
    global cap, paused, frame1
    if not paused:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (SET_WIDTH, SET_HEIGHT))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            canvas.create_image(0, 0, image=frame, anchor=NW)
            canvas.image = frame  # Keep a reference
            frame1 = cap.get(cv2.CAP_PROP_POS_FRAMES)

        else:
            cap.release()
            paused = True
    if not paused:
        window.after(15, update_frame)

```
#### Pending Video Playback Function:
```python
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
```

![Screenshot 2024-12-30 172746.png](Screenshot%202024-12-30%20172746.png)

#### Video Playback Control Buttons:
```python
# Buttons for video control
btn1 = Button(window, text="<<Fast Backwards", width=50, command=partial(play, -25))
btn1.pack()

btn6 = Button(window, text="<<Backwards(1 frame)", width=50, command=partial(play, -5))
btn6.pack()

btn2 = Button(window, text="Fast Forward >>", width=50, command=partial(play, 25))
btn2.pack()

btn7 = Button(window, text="Forward(1 frame)>>", width=50, command=partial(play, 5))
btn7.pack()

btn3 = Button(window, text="Pause", width=50, command=pause)
btn3.pack()

btn4 = Button(window, text="OUT", width=50, command=out)
btn4.pack()

btn5 = Button(window, text="NOT OUT", width=50, command=not_out)
btn5.pack()
```


### Testing and Optimization:

- The system was tested with cricket match footage to validate functionality.

- Performance metrics such as playback smoothness and interface responsiveness were evaluated.

## Challenges

- Ensuring real-time performance without lag during high-resolution video playback.

- Designing an interface that balances simplicity with comprehensive functionality.

# Results

The Decision Review System successfully demonstrated its ability to:

- Load and process cricket match footage with high accuracy and efficiency.

- Provide operators with precise control over playback and frame navigation.

- Facilitate accurate decisions through clear and intuitive annotations and overlays.

User feedback highlighted the interface’s simplicity and effectiveness, while testing revealed minimal latency and robust performance under various conditions. The project lays a strong foundation for further enhancements, such as integrating advanced trajectory prediction and AI-driven decision support.

![Screenshot 2024-12-30 173104.png](Screenshot%202024-12-30%20173104.png)

![Screenshot 2024-12-30 185328.png](Screenshot%202024-12-30%20185328.png)
## Conclusion

The developed Decision Review System showcases the potential of Python, Tkinter, and OpenCV to create practical and reliable tools for sports analysis. Future work will focus on expanding its capabilities and testing in live match scenarios to further validate its effectiveness, Incorporating AIML techniques to further enhance the system's autonomy, enabling it to learn from past decisions and adapt to new situations without requiring constant manual input. 