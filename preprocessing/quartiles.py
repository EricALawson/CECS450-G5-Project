import preprocessing.additional_participant_data as apd
import preprocessing.fixation_ratio as fr
import pandas as pd

def calc_quartiles(df):
    #df = apd.get_meta_data()
    #df = fr.add_fix_ratio(df)
    df = df.drop('ID', axis=1)

    first_quartile = df.groupby('Category').quantile(0.25).reset_index()
    second_quartile = df.groupby('Category').quantile(0.5).reset_index()
    third_quantile = df.groupby('Category').quantile(0.75).reset_index()
    #print(df)
    return pd.concat([first_quartile, second_quartile, third_quantile])

if __name__ == "__main__":
    df = calc_quartiles()
    print(df)