from picamera import PiCamera
from time import sleep
from datetime import datetime
from tkinter import *

def selectMode(mode):

    if mode == "o":
        #Start preview
        print("In preview only mode")
        camera.start_preview()
        sleep(15)
        camera.stop_preview() 

    if mode == "p":
        print("In photo mode")
        camera.capture(strSaveLoc + datetime.now().strftime("%m%d-%H%M%S") + ".jpg")

    if mode == "v":
        print("In video mode")
        camera.start_recording(strSaveLoc + datetime.now().strftime("%m%d-%H%M%S") + ".h264")
        camera.wait_recording(10)
        camera.stop_recording()
       
    print("finished running selected mode")

# Main code starts below ....
print("Start using your camera")

strSaveLoc = "/home/pi/DEV/Result/"
print("Images can be found in " + strSaveLoc)

root = Tk()
root.title("Photo or Video?")
root.geometry("300x150")

# Get the requested values of the height and widht
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the screen
root.geometry("+{}+{}".format(positionRight, positionDown))

label= Label(root, text='Select a mode', font = "20")
label.pack()

previewOnly = Button(root, text="Preview ONLY", fg = "Black", bg = "white", command=lambda: selectMode("o"))
previewOnly.pack(side = 'top')

takePhoto = Button(root, text="Take a photo", fg = "Black", bg = "White", command=lambda: selectMode("p"))
takePhoto.pack(side = 'top')

takeVideo = Button(root, text="Take a video", fg = "Black", bg = "white", command=lambda: selectMode("v"))
takeVideo.pack(side = 'top')

#Set up
camera = PiCamera()
camera.resolution = (1024, 768)
    
#Start the GUI
root.mainloop()

print("Done")
