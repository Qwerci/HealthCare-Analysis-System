import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the specified file path.
    The dataset is semicolon-seperated, so we use `sep=';'`.
    """
    try:
        data = pd.read_csv(file_path, sep=';')
        print("Dataset loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
    

def clean_and_preprocess(data):
    """
    Perform data cleaning and preprocessing steps:
    1. Convert age from days to years.
    2. Calculate BMI.
    3. Handle missing values.
    4. Handle outliners in blood pressure and BMI.
    """
    print("\nStarting data cleaning and preprocessing...")

    data['age'] = data['age']/365
    print("Age converted from days to years.")

    data['bmi'] = data['weight']/ (data['height'] / 100) ** 2
    print("BMI calculated.")

    if data.isnull().sum().any():
        print("Missing values found. Handling missing values....")
        data.fillna(data.median(), inplace=True)
        print("Missing values filled with median.")
    else:
        print("No missing values found")

    # handle outliners in blood pressure
    # Systolic BP should be between 90 and 250 mmHg, Diastolic BP between 60 and 150 mmHg
    print("Handling outliers in blood pressure...")
    initial_rows = len(data)
    data = data[(data['ap_hi'] >= 90) & (data['ap_hi'] <= 250)]
    data = data[(data['ap_lo'] >= 60) & (data['ap_lo'] <= 150)]
    removed_rows = initial_rows - len(data)
    print(f"Removed {removed_rows} rows with unrealistic blood pressure values.")
    

    # Handle outliers in BMI (BMI should be between 10 and 50)
    print("Handling outliers in BMI...")
    initial_rows = len(data)
    data = data[(data['bmi'] >= 10) & (data['bmi'] <= 50)]
    removed_rows = initial_rows - len(data)
    print(f"Removed {removed_rows} rows with unrealistic BMI values.")
    
    print("Data cleaning and preprocessing completed!")
    return data