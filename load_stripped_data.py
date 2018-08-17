import pandas as pd
import numpy as np
import datetime
from os import listdir
from os.path import isfile, join
import os, shutil
from tqdm import tqdm

headerNames = ['Altitude', 'EastWind', 'NorthWind', 'VerticalWind']
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_rows', 15)

def load_file(filepath):

    filename = filepath.split('/')[-1]
    datanum = filename.split('_')[1]
    seconds = int(filename.split('_')[2][0:-1])

    df = pd.read_csv(filepath, header=0, names=headerNames)
    df['deltaT'] = seconds
    df['dataNum'] = datanum

    # print(datanum)
    #
    # print(seconds)

    return df

def load_path(path):

    # Get all file name is directory and sort
    dataFileNames = [f for f in listdir(path) if
                           isfile(join(path, f)) and f.split('.')[-1] == 'txt']
    dataFileNames = sorted(dataFileNames, key = lambda x: int(x.split('_')[1]))

    dataTimes = [int(x.split('_')[2][0:-1]) for x in dataFileNames ]

    df = pd.DataFrame()

    print("Loading data...")
    for f in tqdm(dataFileNames):
        filepath = path + f

        df_ = load_file(filepath)

        df = df.append(df_)

    # diff_t = np.diff(dataTimes)
    #
    # for (idx, delta) in enumerate(diff_t):
    #     # print(idx, delta)
    #     if delta > 50:
    #         print(idx, delta)
    #
    # # print(dataTimes)
    return df

def load_path_df_list(path):

    # Get all file name is directory and sort
    dataFileNames = [f for f in listdir(path) if
                           isfile(join(path, f)) and f.split('.')[-1] == 'txt']
    dataFileNames = sorted(dataFileNames, key = lambda x: int(x.split('_')[1]))

    dataTimes = [int(x.split('_')[2][0:-1]) for x in dataFileNames ]


    df_list = []
    print("Loading data...")
    for f in tqdm(dataFileNames):
        filepath = path + f

        df_ = load_file(filepath)

        df_list.append(df_)

    # diff_t = np.diff(dataTimes)
    #
    # for (idx, delta) in enumerate(diff_t):
    #     # print(idx, delta)
    #     if delta > 50:
    #         print(idx, delta)
    #
    # # print(dataTimes)
    return df_list

def load_pickle(filepath):
    return pd.read_pickle(filepath)


def getRGAN_data(dataPath, nseq):
    df_list = load_path_df_list(dataPath)

    nsamples = len(df_list)
    wind_data = np.zeros([nsamples, nseq, 1])
    alts = None

    for idx, df_ in enumerate(df_list):
        df = df_.head(nseq)
        Wnorth = df["NorthWind"].values

        # Weast = df["EastWind"].values
        if idx == 0:
            alts = df["Altitude"].values
        elif np.array_equal(alts, df["Altitude"].values) == False:
            continue  # drop files with screwed up altitudes

            # assert(np.array_equal(alts, df["Altitude"].values)) # Throw error if not all having the same altitudes

        wind_data[idx, :, 0] = Wnorth
        # wind_data[idx,:,1] = Weast

    return wind_data, nsamples

if __name__ == "__main__":
    # dataPath = 'data/stripped/'
    #filename = 'StrippedWind_2_35s_dt.txt'

    dataPath = '../../Data/stripped_wind_groups/group_1/'

    picklename = "StrippedWind.pkl"


    # print(load_file(dataPath+filename))

    # df = load_path(dataPath)

    # df.to_pickle(dataPath + "StrippedWind.pkl")

    # print(load_pickle(dataPath+picklename))

    # print(load_path_df_list(dataPath))

    print(getRGAN_data(dataPath, 100))