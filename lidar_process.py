#Import thư viện cần sử dụng
from rplidar import RPLidar
import numpy as np
# Khởi tạo lidar và list chứa data nhận vào từ lidar
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
        
# Hàm tính toán tọa độ x và y với mỗi angle và distance thu được từ lidar
def compute(angle, distance):
    angle = np.deg2rad(angle)
    x = np.sin(angle)*distance
    y = np.cos(angle)*distance
    return x,y
xy=[compute(angle,distance) for angle,distance in data]

#Chạy hàm thu dữ liệu
get_data()





