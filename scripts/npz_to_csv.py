import os
from os.path import isfile

import numpy as np
import pandas as pd

OUTPUT_DIR = 'outputs'


def convert_npz_to_csv(npz_file, frame_name):
    # Load the NPZ file
    data = np.load(npz_file)
    # List all arrays in the NPZ file
    print(data.files)

    # Access a specific array
    array = data[frame_name]

    df = pd.DataFrame(array)
    df.to_csv(f'result-{npz_file}.csv', index=False)  # save to csv, with name


if __name__ == "__main__":
    for file in os.listdir(OUTPUT_DIR):
        file_path = os.path.join(OUTPUT_DIR, file)
        if isfile(file_path) and file.endswith('.npz'):
            convert_npz_to_csv(file_path, 'arr_0')
