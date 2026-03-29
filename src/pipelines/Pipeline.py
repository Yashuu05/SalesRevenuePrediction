from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from utils.load_data import read_data
from sklearn.impute import SimpleImputer

def create_pipeline(file_path):

    """
    This function creates the pipeline 
    """
    # read data
    df = read_data(path=file_path)

    # find categorical and numerical data
    cat_cols = []
    num_cols = []
    for cols in df.columns:
        if df[cols].dtypes == "object":
            cat_cols.append(cols)
        else:
            num_cols.append(cols)
    
    print("categorical cols = \n", cat_cols)
    print("numerical cols = \n", num_cols)

    # create the pipeline
    print("creating pipeline...")

    cat_preprocessor = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    num_preprocessor = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    pipeline = ColumnTransformer(transformers=[
        ('cat', cat_preprocessor, cat_cols),
        ('num', num_preprocessor, num_cols)
    ], remainder='passthrough'
    )

    return pipeline