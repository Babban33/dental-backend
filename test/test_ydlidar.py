import serial

# Define the serial port (change it based on your configuration)
serial_port = '/dev/YDLidar-SDK'
serial_baudrate = 115200

# Open the serial port
ser = serial.Serial(serial_port, serial_baudrate)

# Read data from the YDLIDAR
while True:
    data = ser.readline()
    print(data.decode('utf-8'))
