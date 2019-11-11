import pandas as pd
import os
import preprocessing.additional_participant_data as meta_data


data_dir = '../eye_tracking_data'
suffix = {1:'.treeFXD.txt', 2:'.graphFXD.txt'}

def fix_ratio(row):
    dir = row['ID']
    path = os.path.join(data_dir, dir)
    if os.path.isdir(path):
        fix_path = os.path.join(path, dir + suffix[row['Visualization']])
        fixColNames = ["number", "time", "duration", "x", "y"]
        fix_data = pd.read_csv(fix_path, names=fixColNames, delimiter='\t', header=None)
        ratio = fix_data['duration'].sum() / fix_data['time'].max()
        return ratio

def add_fix_ratio(aggData):
    print(aggData)
    aggData['Fixation_Ratio'] = aggData.apply(lambda row: fix_ratio(row), axis=1)
    return aggData


if __name__ == "__main__":
    df = meta_data.get_meta_data()
    df2 = add_fix_ratio(df)
    print(df2)
    p_success = df2['Task_Success'].corr(df2['Fixation_Ratio'])
    p_time = df2['Time_On_Task'].corr(df2['Fixation_Ratio'])
    print("Correlation with success: ", p_success)
    print("Correlation with time: ", p_time)