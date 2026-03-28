import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.FeatureEngg import perform_feature_engineering

if __name__ == "__main__":

    print("========== Train dataset ==========")
    # perform feature engineering for train dataset
    file_1 = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cleaned_train.csv')
    save_file_path_1  = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'final_train.csv')
    df_1 = perform_feature_engineering(file_path=file_1)
    df_1.to_csv(save_file_path_1, index=False)
    
    print("\n========== Test dataset ============")
    # perform fetaure engg on test dataset
    file_2 = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cleaned_test.csv')
    save_file_path_2 = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'final_test.csv')
    df_2 = perform_feature_engineering(file_path=file_2)
    df_2.to_csv(save_file_path_2, index=False)
    