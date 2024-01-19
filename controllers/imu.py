"""
    Made by Monnapse
"""

import lib.vector3 as vector3

class new:
    def __init__(self) -> None:
        self.rotation = vector3.new()
        self.position = vector3.new()
        self.temperature = 0

        self.rotation_calibrated_vector = vector3.new()
        self.position_calibrated_vector = vector3.new()
        
    #def calibrate():

    def add_rotation(self, vector: vector3):
        result = self.rotation + vector
        if not result: return
        self.rotation = result

    def data_to_vector3(self,data: {}) -> vector3:
        if not data: return
        if not data["X"] or not data["Y"] or not data["Z"]: return
        return vector3.new(data["X"], data["Y"], data["Z"])

    def get_calibrated_rotation(self, vector3):
        return vector3 - self.rotation_calibrated_vector

    def get_filtered_rotation(self, data: {}) -> vector3:
        vector = data
        if isinstance(data, dict):
            # Dictionary
            vector = self.data_to_vector3(data)
        #else:
            # Vector3
        #return self.data_to_vector3(data)
        vector_calibrated = self.get_calibrated_rotation(vector) # Get Calibrated Value
        print(vector_calibrated)
        return vector_calibrated
    
    def apply_imu_data(self, data: {}):
        if not data: return
        #if data["A"]:
        #    # Acceleration
        if data["R"]:
            # Rotation
            rot_vector = self.data_to_vector3(data["R"])
            if not rot_vector: return
            print(self.get_filtered_rotation(data["R"]))
            #self.add_rotation(rot_vector)
            #print(self.rotation)