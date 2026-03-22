import pandas as pd 
import logging

def read_data(path):
    try: 
        df = pd.read_csv(path)
        logging.info(f"read {path} data")
        print(f"{path} dataset loaded successfully!")
        return df
    except Exception as e:
        logging.error(f"{e}")
        print(f"error! {e}")
        