import matplotlib.pyplot as plt
import numpy as np
import lidar_process as lp

#check when lidar move around the room, if the point cloud is duplicate, remove it
def remove_duplicate(data):
    new_data = []
    for i in range(len(data)):
        if i == 0:
            new_data.append(data[i])
        else:
            if data[i] != data[i-1]:
                new_data.append(data[i])
    return new_data


