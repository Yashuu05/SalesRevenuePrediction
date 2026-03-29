import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.pipelines.ModelPipeline import create_model_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, root_mean_squared_error
from utils.load_data import read_data
##################################################################################################

def model_architecture():

    """
    This function creates the pipeline for each model
    Output: List of model pipelines
    """

    # linear Regression
    lr_model = LinearRegression(fit_intercept=True, n_jobs=-1)
    lr_pipeline = create_model_pipeline(model=lr_model)

    # SVR
    svr_model = SVR(kernel='rbf', C=1.0, gamma='scale', verbose=False)
    svr_pipeline = create_model_pipeline(model=svr_model)

    # Decision Tree
    dt_model = DecisionTreeRegressor(criterion='squared_error', splitter='best', max_depth=7, min_samples_split=2)
    dt_pipeline = create_model_pipeline(model=dt_model)

    # Random Forest Classifier
    rf_model = RandomForestRegressor(criterion='squared_error', n_estimators=200, max_depth=7, random_state=42, n_jobs=-1)
    rf_pipeline = create_model_pipeline(model=rf_model)

    # XGBoostRegressor
    xgb_pipeline = create_model_pipeline(model=XGBRegressor())

    model_list = [lr_pipeline, svr_pipeline, dt_pipeline, rf_pipeline, xgb_pipeline]

    return model_list

################################################################################################
def train_model(models, X_train, y_train, X_test, y_test):

    """
    This function is responsible to train and calculate the performance
    of the ML models specified.
    Input: Model pipeline
    output: Model Performance
    """
    try:
        print("====== Training Models =====")
        model_performance = {}
        for model in range(len(models)):

            print(f"\n{model}. fitting {models[model]}...")
            # fit the model
            models[model].fit(X_train, y_train)
            # predict the tareget valraible
            y_pred = models[model].predict(X_test)
            # calculate performance metrics
            r2 = r2_score(y_test, y_pred)
            rmse = root_mean_squared_error(y_test, y_pred)

            print(f"r2 score: {r2:.4f}  |  rmse : {rmse:.4f}")
            # Store the performance in a dictionary
            model_performance[models[model]] = rmse
            
        return model_performance
    
    except Exception as e:
        print(f"Error training models: {e}")
        return {}
##################################################################################################

if __name__ == "__main__":
    
    # read data
    X_train = read_data(path=os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'X_train.csv'))
    X_test = read_data(path= os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'X_test.csv'))
    y_train = read_data(path=os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'y_train.csv'))
    y_test = read_data(path= os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'y_test.csv'))

    # Replace infinity with NaN so it can be imputed
    import numpy as np
    X_train = X_train.replace([np.inf, -np.inf], np.nan)
    X_test = X_test.replace([np.inf, -np.inf], np.nan)
    
    # Ravel target variables to avoid warnings
    y_train = y_train.values.ravel()
    y_test = y_test.values.ravel()

    # get model list
    list_of_models = model_architecture()
    # train the model
    model_perfromance = train_model(list_of_models, X_train, y_train, X_test, y_test)
    print("\n======== Summary =========")
    for i,j in model_perfromance.items():
        print(f"{i} : {j}\n")
    
    # save performance
    performance_list = []
    for model_obj, rmse in model_perfromance.items():
        # Get the class name of the model if it's a pipeline
        model_name = str(model_obj.named_steps['model'].__class__.__name__)
        performance_list.append({'model': model_name, 'performance': rmse})
        
    model_perfromance_data = pd.DataFrame(performance_list)
    save_file_path =  os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'model_performance.csv')
    model_perfromance_data.to_csv(save_file_path, index=False)
    

