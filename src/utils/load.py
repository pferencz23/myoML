import pandas as pd
import numpy as np
import os

def load_data(data_directory):
    path_mixed_demographics = data_directory + "/mixed_demographics.csv"
    path_all_files = data_directory + "/mixed_samples"

    mixed_demographics_df = pd.read_csv(path_mixed_demographics, index_col=0)

    onlyfiles = [
        os.path.join(path_all_files, f) 
        for f in os.listdir(path_all_files)
        if f.endswith("npy")
    ]

    all_samples = np.empty([900, 10, 18000, 4])
    for i, file_name in enumerate(onlyfiles):
        all_samples[i] = np.load(file_name)

    return mixed_demographics_df, all_samples
