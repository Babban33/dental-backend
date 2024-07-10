import serial
import multiprocessing

def lidar_process(distance_value):
    ser = serial.Serial("/dev/serial0", 115200)

    def getTFminiData():
        while True:
            count = ser.in_waiting
            if count > 8:
                recv = ser.read(9)
                ser.reset_input_buffer()
                if recv[0] == 89 and recv[1] == 89:  # Use decimal values instead of hex
                    low = int(recv[2])
                    high = int(recv[3])
                    distance = low + high * 256
                    distance_value.value = distance

    try:
        if not ser.is_open:
            ser.open()
        getTFminiData()
    except KeyboardInterrupt:   # Ctrl+C
        if ser is not None:
            ser.close()

if __name__ == '__main__':
    distance_value = multiprocessing.Value('i', 0)
    process = multiprocessing.Process(target=lidar_process, args=(distance_value,))
    process.start()
    process.join()