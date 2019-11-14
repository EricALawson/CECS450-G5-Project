import preprocessing.additional_participant_data as apd
import preprocessing.fixation_ratio as fr

def calc_means(df):
    #df = apd.get_meta_data()
    #df = fr.add_fix_ratio(df)

    df = df.groupby('Category').mean().reset_index()
    #print(df)
    return df

if __name__ == "__main__":
    df = calc_means()
    print(df)