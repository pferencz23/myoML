import pandas as pd
import numpy as np
import os

"""EXAMPLE USAGE FOR NOTEBOOKS"""

path_mixed_demographics = "../data/training_data/mixed_demographics.csv"
path_all_files = "../data/training_data/mixed_samples"

mixed_demographics_df = pd.read_csv(path_mixed_demographics, index_col=0)

onlyfiles = [
    os.path.join(path_all_files, f) 
    for f in os.listdir(path_all_files)
    if f.endswith("npy")
]

all_samples = np.empty([900, 10, 18000, 4])
for i, file_name in enumerate(onlyfiles):
    all_samples[i] = np.load(file_name)
