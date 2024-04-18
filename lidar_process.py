#Import thư viện cần sử dụng
from rplidar import RPLidar
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Khởi tạo lidar
lidar = RPLidar('COM5',timeout=3,baudrate=115200)
data = []
# Hàm lấy dữ liệu từ lidar
def get_data():  
    try:
        for scan in lidar.iter_scans():
            for (_, angle, distance) in scan:
                #print(angle, distance)
                data.append((angle, distance))
                print((angle, distance))   
    except KeyboardInterrupt or SystemExit or Exception:
        print('Stop')
        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()
        print('Lidar disconnected')
        print('Data length:',len(data))
        
# Hàm vẽ đồ thị 3D(cái này từ từ làm, do phải đi cùng camera)
get_data()





