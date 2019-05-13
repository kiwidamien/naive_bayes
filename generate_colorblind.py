import pandas as pd
import numpy as np


INPUT = 'raw_data/weight-height.csv'
OUTPUT = 'processed_data/weight-height-color.csv'

np.random.seed(52)

percent_colorblind = {
    'Male': 0.08, 'Female': 0.005
}

def is_colorblind(row):
    return np.random.random() <= percent_colorblind[row['Gender']]


demo = pd.read_csv(INPUT)
demo['colorblind'] = demo.apply(is_colorblind, axis=1)
demo.to_csv(OUTPUT, index=False)
