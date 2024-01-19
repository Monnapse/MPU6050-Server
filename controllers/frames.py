"""
    Made by Monnapse
"""

import time

class Frames:
    def __init__(self, imu_controller, imu, frames_per_second:int=30) -> None:
        self.imu_controller = imu_controller
        self.fps = frames_per_second
        self.frames_queue = []
        self.imu = imu

    def handle_frames(self):
        print("Handle Frames has started")
        global framesQueue
        global first_frames
        #time.sleep(1)
        while True:
            try:
                frame = self.frames_queue.pop(0)
                #c.send(bytes(frame, "utf-8"))
                #self.imu_controller.send_data(rotation)
                if frame:
                    #print(frame)
                    self.imu.apply_imu_data(frame)
                    self.imu_controller.send_data(frame)
            
            except:
                pass
            time.sleep(1/self.fps)