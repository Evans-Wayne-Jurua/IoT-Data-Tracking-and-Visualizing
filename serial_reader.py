import serial

ser = serial.Serial('COM4',9600);

while True: 
    data = ser.readline().decode().strip()
    print(data);