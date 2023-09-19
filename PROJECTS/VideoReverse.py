import cv2 as cv


vid = cv.VideoCapture("F:\Project\FaceRecognisation\DataSets\Countdown1_preview.mp4")

Height = vid.get(cv.CAP_PROP_FRAME_HEIGHT)
Width = vid.get(cv.CAP_PROP_FRAME_WIDTH)

FramesRate = vid.get(cv.CAP_PROP_FPS)
Total_frame = vid.get(cv.CAP_PROP_FRAME_COUNT)

FourCC = cv.VideoWriter_fourcc(*'MJPG')

New_vide = cv.VideoWriter("reverse.avi",FourCC,FramesRate,(int(Width),int(Height)))

opend = vid.isOpened()
writeat_Frames= Total_frame-1
if(opend):
    
    while(writeat_Frames!=0):
        #set the surrent frame position to last frame of the video
        vid.set(cv.CAP_PROP_POS_FRAMES,writeat_Frames)
        isTrue,cur_frame = vid.read()
        New_vide.write(cur_frame)
        writeat_Frames=writeat_Frames-1

        if cv.waitKey(20) & 0xFF==ord('d'):  #says is "D" key press than exit the video vindow
            break

New_vide.release()
vid.release()
cv.destroyAllWindows()