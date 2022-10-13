import cv2
vidcap = cv2.VideoCapture('IMG_7237.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*10000))
  success,image = vidcap.read()
  cv2.imwrite("frame%d.jpg" % count, image)     
  count += 1