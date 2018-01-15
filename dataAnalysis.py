import csv
import time as unixTime
import numpy as np
tic = unixTime.time()
filename = 'Jan14_SOS_0.4531'
ext = '.csv'
data = []
time = []
load = []
pressure = []
window = 10
with open(filename+ext) as fp:
    for row in csv.reader(fp):
        time.append(np.array(row[0]))
        load.append(np.array(row[1]))
        pressure.append(np.array(row[2]))

print("data broken into vectors")
print("finding peak load and deleting data around a",window,"second window")

t1 = float(time[0])
t2 = float(time[1])
timeStep = round(t2 - t1,3)

print("data has an approximate time step of "+str(timeStep)+" seconds")

t = 0

for x in time:
    try:
        time[t] = float(time[t])
        load[t] = float(load[t])
        pressure[t] = float(pressure[t])
    except ValueError:
        time[t]=''
        load[t]=''
        pressure[t]=''
    t += 1

time = [x for x in time if x ]
load = [x for x in load if x ]
pressure = [x for x in pressure if x]
print("Non numeric values deleted...")
idxMax = int(np.argmax(load))

timeNew = time[idxMax-round(window/2/timeStep):idxMax+round(window/2/timeStep)]
timeNew[:] = [x - timeNew[0] for x in timeNew]
loadNew = load[idxMax-round(window/2/timeStep):idxMax+round(window/2/timeStep)]
pressureNew = pressure[idxMax-round(window/2/timeStep):idxMax+round(window/2/timeStep)]

newfile = filename + '_truncated' + ext
with open(newfile,'w', newline='') as newfp:
    print("writing to new file...")
    t = 0
    for x in timeNew:
        csvRow = [timeNew[t], loadNew[t], pressureNew[t]]
        wr = csv.writer(newfp)
        wr.writerow(csvRow)
        t += 1
        if t > len(time) + 100:
            break

toc = unixTime.time() - tic
print("done... ",round(toc,2)," seconds elapsed")
