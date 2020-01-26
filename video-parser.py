import cv2

# input video here, 0 for webcam

#cap= cv2.VideoCapture('gtest0.mov')
cap = cv2.VideoCapture(0)

frequency = 10     # higher freq, lower still image outputs
i=0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    
    if (i%frequency==0):
        cv2.imwrite('CLASSIFY_ME.jpg',frame)
    print("Parsing...")
    
    i+=1

cap.release()
cv2.destroyAllWindows()
