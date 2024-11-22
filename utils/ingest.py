import pandas as pd

def ingest_data(file_path: str):
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please use CSV.")
    return data
