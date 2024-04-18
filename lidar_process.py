#Import thư viện cần sử dụng
from rplidar import RPLidar

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
        print('Data length:',len(data))

#Chạy hàm thu dữ liệu
get_data()





