"""
    Made By Monnapse
"""

from flask import Flask, request
import json

import time
import socket
from controllers import imu_socket, routes, frames, imu

# INFO
VERSION = "0.0.2"
routes.VERSION = VERSION

# SETTINGS
PORT = 5375
SOCKET_PORT = 6756
FRAMES = 30

# SERVER
app = Flask(__name__)

imu_controller = imu_socket.new(SOCKET_PORT) # Create socket

_imu = imu.new()

frames_controller = frames.Frames(imu_controller, _imu, FRAMES)

# Create and Start server routes
Route = routes.Route(app, frames_controller)
Route.start_server_routes()

if __name__ == '__main__':
    imu_controller.connect_clients() # Start socket

    print("* Running on port:"+str(PORT))
    app.run(host="0.0.0.0", port=PORT, debug=True)