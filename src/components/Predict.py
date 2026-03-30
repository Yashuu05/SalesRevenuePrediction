import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.LoadModel import load_model
from utils.load_data import read_data
import pandas as pd

def predict(model, X_test):  
    try:
        y_pred = model.predict(X_test)
        predicted_data = pd.DataFrame({
            "sales_revenue": y_pred
        })

        return predicted_data
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # load Test dataset
    X_test = read_data(path=os.path.join(os.path.dirname(__file__), '..', '..', 'data','processed','X_test.csv'))
    # load saved model
    model = load_model(file_path=os.path.join(os.path.dirname(__file__), '..', '..', 'model', 'xgb.pkl'))
    # predict the target varaible
    predicted_data = predict(model=model, X_test=X_test)
    save_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data','predicted','predict.csv')
    # save the data
    predicted_data.to_csv(save_file_path, index=False)