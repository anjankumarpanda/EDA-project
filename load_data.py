import pandas as pd

def load_dataset():
    data = pd.read_csv("data/sample_data.csv")
    return data