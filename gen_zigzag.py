#!/usr/bin/env python3
# Plot data.csv via:
# gnuplot -p -e "set datafile separator ','; plot 'data.csv' using 1 title 'value' with lines, 'data.csv' using 2 title 'avg10' with lines, 'data.csv' using 3 title 'avg50' with lines"
import csv
import numpy as np

def zigzag(start, end, count, volatility=10):
    value = start
    lift = (end - start) / count
    forward = 200
    backward = int(volatility * 50)
    data = []

    # Calculate zigzag body
    for i in range(0, count - backward):
        if i%(forward + backward) < forward:
            value += (forward + 2 * backward) / forward * lift
        else:
            value -= lift
        avg20 = np.average([x['value'] for x in data[-min(len(data), 20):]] + [value])
        avg100 = np.average([x['value'] for x in data[-min(len(data), 100):]] + [value])
        data += [{ 'value': value, 'avg20': avg20, 'avg100': avg100}]
        i += 1

    # Calculate tail as a linear line
    lift = (end - value)/(backward - 1)
    for i in range(count - backward, count):
        value += lift
        avg20 = np.average([x['value'] for x in data[-min(len(data), 20):]] + [value])
        avg100 = np.average([x['value'] for x in data[-min(len(data), 100):]] + [value])
        data += [{ 'value': value, 'avg20': avg20, 'avg100': avg100}]
        i += 1

    return data

if __name__ == '__main__':
    rows = zigzag(start=1, end=1000, count=50000)
    with open('data.csv', 'w') as outputFile:
        csvWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            csvWriter.writerow([
                ('{:.%df}' % 2).format(max(row['value'], 10** - 2)),
                ('{:.%df}' % 2).format(max(row['avg20'], 10** - 2)),
                ('{:.%df}' % 2).format(max(row['avg100'], 10** - 2))
            ])
