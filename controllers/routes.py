"""
    Made by Monnapse
"""

from flask import Flask, request
import json
from threading import Thread
import lib.arrays as arrays

VERSION = "cant load"

first_frames = False

class Route():
    def __init__(self,app: Flask, frames_controller) -> None:
        self.app = app
        self.frames_controller = frames_controller
        pass

    def start_server_routes(self):
        @self.app.route('/')
        def home():
            return {
                "message": "IMU Server is online!",
                "version": VERSION
            }, 200

        @self.app.route('/update', methods=["POST"])
        def update():
            # Globals
            global first_frames

            if not first_frames:
                first_frames = True
                t = Thread(target=self.frames_controller.handle_frames)
                t.start()

            try:
                data = str(request.get_data())
                fixed_string = data.strip("b''")
                json_data = json.loads(fixed_string)
                if not json_data and not json_data["framesQueue"]:
                    return "", 401
                #print(json_data["framesQueue"])
                join = arrays.group_arrays(self.frames_controller.frames_queue, json_data["framesQueue"])

                if join:
                    self.frames_controller.frames_queue = join
                else:
                    return "", 401
                return "", 200
            except Exception:
                return "", 401