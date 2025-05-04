import pandas as pd
import json

def load_data(uploaded_file):
    file_type = uploaded_file.name.split('.')[-1]
    if file_type == 'csv':
        return pd.read_csv(uploaded_file)
    elif file_type == 'json':
        return pd.read_json(uploaded_file)
    elif file_type in ['xls', 'xlsx']:
        return pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file type")

def filter_data(df, selected_cols):
    return df[selected_cols]
