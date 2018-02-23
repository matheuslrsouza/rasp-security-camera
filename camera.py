import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time

class VideoCamera(object):
  def __init__(self):
    # self.video = cv2.VideoCapture(0)
    self.video = PiVideoStream().start()
    time.sleep(2.0)

  def __del__(self):
    self.video_release()

  def get_frame(self):
    #success, image = self.video.read()
    image = self.video.read()

    ret, jpeg = cv2.imencode('.jpg', image)
    return jpeg.tobytes()