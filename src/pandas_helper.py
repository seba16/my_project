from pandas import read_csv

def read_csv_data(data_path):
    if data_path is None or len(data_path) == 0:
        print("La ruta del archivo está vacía")
        return None
    
    try:
        df = read_csv(data_path)
        return df
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo en la ruta: {data_path}")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
    
def clean_data(df):
    if df is None or df.empty:
        print("El dataframe está vacío o es None")
        return None
    
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def change_data_type(df, column_names: list[str], new_type):
    if df is None or df.empty:
        print("El dataframe está vacío o es None")
        return None
    
    if column_names is None or len(column_names) == 0:
        print("La lista de columnas está vacía")
        return df
    
    if new_type is None or len(new_type) == 0:
        print("El tipo de datos está vacío")
        return df
    
    for column in column_names:
        if column in df.columns:
            df[column] = df[column].astype(new_type)
        else:
            print(f"La columna '{column}' no existe en el dataframe")
    return df

def total_sales_by_product_category(df):
    if df is None or df.empty:
        print("El dataframe está vacío o es None")
        return None
    
    required_columns = ["product_category", "total_amount"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"Las siguientes columnas no existen: {missing_columns}")
        print(f"Columnas disponibles: {list(df.columns)}")
        return None

    return df.groupby("product_category")["total_amount"].sum()

def average_sales_by_product_category_by_date(df):
    if df is None or df.empty:
        print("El dataframe está vacío o es None")
        return None
    
    required_columns = ["product_category", "date", "total_amount", "quantity"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"Las siguientes columnas no existen: {missing_columns}")
        print(f"Columnas disponibles: {list(df.columns)}")
        return None
    
    return df.groupby(["product_category", "date"])["quantity"].mean()

def group_sales_by_product_category(df):
    if df is None or df.empty:
        print("El dataframe está vacío o es None")
        return None
    
    return df.groupby("product_category")["quantity"].sum()

def get_sales_by_category(df, category):
    if df is None or df.empty:
        print("El dataframe está vacío o es None")
        return None
    
    return df[df["product_category"] == category]["total_amount"].sum()