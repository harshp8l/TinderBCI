from NeuroPy import NeuroPy
import keyboard
import csv
import mindwave
import datetime
import time
import numpy as np

# returns a list with avgs and std devs of features
def calcAvgAndStdDev(queue):
    finalfeat = []

    #dropping time and converting to floats
    data = np.array(np.asarray(queue)[:,1:], dtype='float32')

    finalfeat += np.average(data, axis=0).tolist()
    finalfeat += np.std(data, axis=0).tolist()
    return finalfeat

# continuously populates queue with relevant features
def populate(queue):
    rowdata = []
    rowdata.append(datetime.datetime.now())
    rowdata.append(hset.rawValue)
    rowdata.append(hset.attention)
    rowdata.append(hset.meditation)
    rowdata.append(hset.delta)
    rowdata.append(hset.theta)
    rowdata.append(hset.lowAlpha)
    rowdata.append(hset.highAlpha)
    rowdata.append(hset.lowBeta)
    rowdata.append(hset.highBeta)
    rowdata.append(hset.lowGamma)
    rowdata.append(hset.midGamma)
    queue.append(rowdata)

# NeuroSky Setup
hset = NeuroPy('COM4')
hset.start()
time.sleep(8)
print('Ready...')

results = []
queue = []
while True:

    # Terminating data collection
    if keyboard.is_pressed('q'):
        print('Quitting - Results outputted to output.csv')
        #storing into csv
        with open("output.csv", "wb") as f:
            writer = csv.writer(f)
            writer.writerows(results)
        break


    # Populating queue with brainwave data and Maxing queue limit to 3 seconds
    populate(queue)
    if (queue[-1][0] - queue[0][0]).total_seconds() >= 3.0:
        queue.pop(0)

    # Gathering datapoint for a rightswipe and cleaning queue
    if keyboard.is_pressed('right'):
        print('right')
        dpoint = calcAvgAndStdDev(queue) + ['right']
        results.append(dpoint)
        queue = []
        time.sleep(1)

    # Gathering datapoint for a leftswipe and cleaning queue
    if keyboard.is_pressed('left'):
        print('left')
        dpoint = calcAvgAndStdDev(queue) + ['left']
        results.append(dpoint)
        queue = []
        time.sleep(1)
