import pandas as pd
import os
import preprocessing.additional_participant_data as meta_data
import math


data_dir = '../eye_tracking_data'
suffix = {1:'.treeFXD.txt', 2:'.graphFXD.txt'}

def createAngles(points):
    angles = []
    for i in range(len(points) - 2):
        angles.append((points[i], points[i + 1]))

    return angles

# 1280x1024

def scanpath(row):
    dir = row['ID']
    path = os.path.join(data_dir, dir)
    if os.path.isdir(path):
        fix_path = os.path.join(path, dir + suffix[row['Visualization']])
        fixColNames = ["number", "time", "duration", "x", "y"]
        fix_data = pd.read_csv(fix_path, names=fixColNames, delimiter='\t', header=None)
        a = fix_data['x']
        b = fix_data['y']

    saccade_length = []

    for i in range(len(a) - 1):
        # Get first x and y coordinates
        x1 = a[i]
        x2 = a[i + 1]

        # Get second x and y coordinates
        y1 = b[i]
        y2 = b[i + 1]

        # Calculate saccade length
        # Divide by 75 DPI to convert pixels to inches
        distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)) / 75
        saccade_length.append(distance)

    scanpath_length = sum(saccade_length)
    return scanpath_length


def add_scanpath_length(aggData):
    #print(aggData)
    aggData['Scanpath_length'] = aggData.apply(lambda row: scanpath(row), axis=1)
    return aggData


if __name__ == "__main__":
    df = meta_data.get_meta_data()
    df2 = add_scanpath_length(df)
    print(df2)


