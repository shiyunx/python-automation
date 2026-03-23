# Import libraries
import pandas as pd
import os

# Define function
def data_cleaning(file_path):

    # Check file
    if not os.path.exists(file_path):
        print("File not found")
        return None, None

    # Split into file name and extension
    file_ext = os.path.splitext(file_path)[1].lower()
    
    # Check file extension
    if file_ext == '.csv':
        df = pd.read_csv(file_path)
    elif file_ext == '.xlsx':
        df = pd.read_excel(file_path, engine='openpyxl')
    else:
        print("Invalid file.")
        return None, None

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Standardise column names: lowercase, underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Check text columns
    str_cols = df.select_dtypes(include='object').columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()  # Trim whitespace
        df[col] = df[col].replace(['', 'NaN'], 'Unknown')
        df[col] = df[col].fillna('Unknown')

    # Check numeric columns
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric
        if 'count' in col.lower() or 'num' in col.lower():
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna(df[col].median())

    # Save cleaned file
    cleaned_file = f"cleaned_{os.path.basename(file_path)}"
    if file_ext == '.csv':
        df.to_csv(cleaned_file, index=False, na_rep='Unknown')
    else:
        df.to_excel(cleaned_file, index=False)

    print(f"Data cleaning saved: {cleaned_file}")
    return cleaned_file, df

# Run script
if __name__ == "__main__":
    # User input
    file_path = input("File path: ")
    
    # Call data_cleaning function
    cleaned_file, cleaned_df = data_cleaning(file_path)
    
    # Check data_cleaning status
    if cleaned_file:
        print("Data cleaning completed")