import serial, time, csv
# establish connection to the serial port that your arduino
# is connected to.
ser = serial.Serial('COM3', 9600, timeout=1)
print("connected to: " + ser.portstr)
t = 0
filename = 'dataFile.csv'
tic = time.time()
with open(filename, 'w', newline='') as fp:
    print("writing to", filename)
    while (1):
        t = t + 1
        # reads the incoming data and converts it from b'xxx'r\n\ to a str
        line = ser.readline()
        data = line.strip().decode()
        now = time.time()

        # write to file=======================
        csvRow = [now, data]
        wr = csv.writer(fp)
        wr.writerow(csvRow)

        if t == 1000:
            break
toc = time.time() - tic
print("Data collection complete.",toc,"seconds elapsed.")
ser.close()
