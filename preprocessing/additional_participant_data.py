import pandas as pd
import numpy as np

def categorize(row):
    if row['Ontologies']==1 and row['Visualization']==1:
        return 1 #"TreeEasy"
    elif row['Ontologies']==2 and row['Visualization']==1:
        return 2 #"TreeHard"
    elif row['Ontologies']==1 and row['Visualization']==2:
        return 3 #"GraphEasy"
    elif row['Ontologies']==2 and row['Visualization']==2:
        return 4 #"GraphHard"
    else: return 0

def get_meta_data():
    df = pd.read_csv("../eye_tracking_data/Additional Participant Data.csv")


    df['Category'] = df.apply(lambda row: categorize(row), axis =1)
    return df

if __name__ == "__main__":
    print(get_meta_data())

