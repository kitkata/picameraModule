from picamera import PiCamera
from time import sleep
from datetime import datetime
from tkinter import *

def selectMode(mode):

    if mode == "o":
        print("In preview only mode")
        camera.start_preview(fullscreen=False,window=(350,100,1024,768))

        for effect in camera.IMAGE_EFFECTS:
            camera.image_effect = effect
            camera.annotate_text = "Effect: %s" % effect
            sleep(5)
            
        camera.stop_preview() 

    if mode == "p":
        print("In photo mode")
##        camera.capture(strSaveLoc + "{counter:03d}.jpg")
        camera.capture(strSaveLoc + datetime.now().strftime("%m%d-%H%M%S") + ".jpg")

    if mode == 'tl':
        print("In timelapse mode")
        camera.start_preview(fullscreen=False,window=(350,100,1024,768))
        try:
            for i, filename in enumerate(camera.capture_continuous(strSaveLoc + "img{timestamp:%m%d}{counter:02d}.jpg")):
                print('Captured %s' % filename)
                camera.annotate_text = 'Captured %s' % filename
                sleep(5)
                if filename[-6:] == "03.jpg":
                    break
        finally:
            camera.stop_preview()

    if mode == "v":
        print("In video mode")
        camera.video_stabilization = True
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
root.geometry("500x400")

# Get the requested values of the height and widht
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the screen
root.geometry("+{}+{}".format(positionRight, positionDown))

# Set up pane
pane = Frame(root)
pane.pack(fill=BOTH, expand = True)

# Create title
label= Label(pane, text='Select a mode', font = "20")
##label= Label(root, text='Select a mode', font = "20")
label.pack()

# Create all the buttoms
previewOnly = Button(pane, text="Preview ONLY", fg = "Black", bg = "pink", command=lambda: selectMode("o"))
takePhoto = Button(pane, text="Take a photo", fg = "Black", bg = "lightskyblue", command=lambda: selectMode("p"))
takeTimelapse = Button(pane, text="Take timelapse photos (5s)", fg = "Black", bg = "lavenderblush", command=lambda: selectMode("tl"))
takeVideo = Button(pane, text="Take a video", fg = "Black", bg = "moccasin", command=lambda: selectMode("v"))

# Pack all the buttoms
previewOnly.pack(side = 'top', fill=BOTH, expand = True)
takePhoto.pack(side = 'left', fill=BOTH, expand = True)
takeTimelapse.pack(side = 'left', fill=BOTH, expand = True)
takeVideo.pack(side = 'top', fill=BOTH, expand = True)

#Set up
camera = PiCamera()
camera.resolution = (1024, 768)   # max is 2592 x 1944
camera.rotation = 90
camera.sharpness = 20
    
#Start the GUI
root.mainloop()

print("Done")
