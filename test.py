import cv2


video1 = cv2.VideoCapture ('input/RPReplay_Final1635523941.MP4')
video2 = cv2.VideoCapture('input/RPReplay_Final1635531085.MP4')
video3 = cv2.VideoCapture('input/RPReplay_Final1635619424.MP4')
# print(video1, video2, video3)

if not video1.isOpened():
    print('error')


while video1.isOpened():
    ret, frame = video1.read()

    if ret == True:
        cv2.imshow('Frame', frame)
    
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

video1.release()
cv2.destroyAllWindows()
print('done')

