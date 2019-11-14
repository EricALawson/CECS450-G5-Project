#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:17:01 2019

@author: sanyoon
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:54:00 2019

@author: https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
"""

import numpy as np
import pandas as pd
import os
import preprocessing.additional_participant_data as meta_data
import scipy.spatial as sp

data_dir = '../eye_tracking_data'
suffix = {1:'.treeFXD.txt', 2:'.graphFXD.txt'}

def convex_hull(row):
    dir = row['ID']
    path = os.path.join(data_dir, dir)
    if os.path.isdir(path):
        fix_path = os.path.join(path, dir + suffix[row['Visualization']])
        fixColNames = ["number", "time", "duration", "x", "y"]
        fix_data = pd.read_csv(fix_path, names=fixColNames, delimiter='\t', header=None)
        a = fix_data['x']
        b = fix_data['y']
        return PolyArea(a,b)
    
        
def add_convex_hull(aggData):
    print(aggData)
    aggData['Convex Hull Area'] = aggData.apply(lambda row: convex_hull(row), axis=1)
    return aggData



def PolyArea(x,y):
    #return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
    points = list(zip(x, y))
    #print(points)
    relevant_points = [ point for point in points if point[1] > 400] #point[1] is y, 400 is estimated end of a UI element on the screen
    return sp.ConvexHull(relevant_points).volume




#print ("Area of Convex Hull = " + str(PolyArea(x,y)))    


if __name__ == "__main__":
    df = meta_data.get_meta_data()
    df2 = add_convex_hull(df)
    print(df2)
    print(df2['Convex Hull Area'].max())

    
