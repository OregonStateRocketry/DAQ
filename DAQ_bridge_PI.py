import serial, time, csv
from serial.tools import list_ports

p = list_ports.comports()
for ports in p:
    print(ports)
# establish connection to the serial port that your arduino
# is connected to.

ser = serial.Serial('/dev/ttyACM1', 115200, timeout=1)
ser.reset_input_buffer()
ser.reset_output_buffer()
print("connected to: " + ser.portstr)
t = 0
filename = 'Jan13_SOS_0.4531.csv'

with open(filename, 'w',newline='', errors='replace') as fp:
    time.sleep(1)
    tic = time.time()
    print("writing to", filename)
    while (1):
        t = t + 1
        # reads the incoming data and converts it from b'xxx'r\n\ to a str        
        line = ser.readline()
        data = line.strip().decode(errors='ignore').split(",")
        now = time.time() - tic
        # write to file=======================
        if t > 5:
		try: 
            		csvRow = [now,data[0],data[1]]
		except IndexError:
			pass
		continue
            wr = csv.writer(fp)
            wr.writerow(csvRow)
            print(csvRow)
        if now > 10**60:
            break
toc = time.time() - tic
print("Data collection complete.",toc,"seconds elapsed.")
ser.close()

