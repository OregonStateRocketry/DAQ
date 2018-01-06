import serial, time, csv
from serial.tools import list_ports

p = list_ports.comports()
for ports in p:
    print(ports)
# establish connection to the serial port that your arduino
# is connected to.

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
print("connected to: " + ser.portstr)
t = 0
filename = 'dataFile.csv'

with open(filename, 'w', newline='') as fp:
    time.sleep(1)
    tic = time.time()
    print("writing to", filename)
    while (1):
        t = t + 1
        # reads the incoming data and converts it from b'xxx'r\n\ to a str
        line = ser.readline()
        data = line.strip().decode().split(",")
        now = time.time() - tic

        # write to file=======================
        csvRow = [now,data[0],data[1]]
        wr = csv.writer(fp)
        wr.writerow(csvRow)

        if now > 3:
            break
toc = time.time() - tic
print("Data collection complete.",toc,"seconds elapsed.")
ser.close()

