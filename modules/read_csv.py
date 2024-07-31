import pandas as pd


def read_broad(file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        print("CSV file has been read successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def read_symbols_from_csv(csv_path):
    # Read the CSV file into a DataFrame
    df = read_broad(csv_path)
    # Extract the values in the 'SYMBOL' column and convert them into an array of strings
    symbols = df['Symbol'].tolist()
    return symbols


def read_symbols_and_industries_from_csv(csv_path):
    # Read the CSV file into a DataFrame
    df = read_broad(csv_path)
    # Extract the values in the 'SYMBOL' and 'industry' columns and convert them into a dictionary
    symbols_and_industries = dict(zip(df['Symbol'], df['Industry']))
    return symbols_and_industries


def read_indice(file_path):
    try:
        # Read the csv file into a DataFrame
        df = pd.read_csv(file_path)
        print("CSV file has been read successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def filter_dataframe_by_index_name(df):
    # Define the values to filter by
    filter_values = ['Nifty 50', "Nifty Auto", "Nifty Bank", "Nifty Energy", "Nifty Financial Services", "Nifty FMCG",
                     "Nifty IT", "Nifty Media", "Nifty Metal", "Nifty MNC", "Nifty Pharma", "Nifty PSU Bank",
                     "Nifty Realty", "Nifty India Consumption", "Nifty Infrastructure", "Nifty PSE",
                     "Nifty Services Sector", "Nifty CPSE", "Nifty Private Bank", "Nifty Oil & Gas",
                     "Nifty Healthcare Index", "Nifty India Digital", "Nifty Consumer Durables",
                     "Nifty India Manufacturing", "Nifty Commodities"]
    # Filter the dataframe
    filtered_df = df[df['Index Name'].isin(filter_values)]

    return filtered_df


def calculate_volume_increment(df1, df2):
    # Merge the two dataframes on Index Name
    merged_df = pd.merge(df1, df2, on='Index Name', suffixes=('_df1', '_df2'))

    # Calculate the volume increment for each Index Name
    merged_df['Volume Increment'] = round(merged_df['Volume_df2'].astype(int) / merged_df['Volume_df1'].astype(int), 2)
    merged_df['Change(%)_df1'] = round(merged_df['Change(%)_df1'].astype(float), 2)
    merged_df['Change(%)_df2'] = round(merged_df['Change(%)_df2'].astype(float),2)

    return merged_df[['Index Name','Change(%)_df1','Change(%)_df2', 'Volume Increment']]


def sort_dataframe(df, column_name, ascending=False):
    # Sort the dataframe based on the specified column
    sorted_df = df.sort_values(by=column_name, ascending=ascending)

    return sorted_df


def read_stock(file_path):
    try:
        # Read the csv file into a DataFrame
        df = pd.read_csv(file_path)
        print("CSV file has been read successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def filter_series_eq(df, symbol_sector_set):
    """
    Filters the DataFrame to include only rows where the SERIES column has value 'EQ'.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: The filtered DataFrame.
    """
    filtered_df = df[df[' SERIES'] == ' EQ']

    # Extract symbols from the set to filter the dataframe
    symbols_to_filter = list(symbol_sector_set.keys())

    # Filter the dataframe based on symbols_to_filter
    filtered_df = df[df['SYMBOL'].isin(symbols_to_filter)]
    return filtered_df


def replace_series_based_on_symbol(df, symbol_replacements):
    """
    Replaces the SERIES column values in the DataFrame based on matching SYMBOL values
    with the provided symbol_replacements dictionary.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    symbol_replacements (dict): Dictionary with SYMBOL as key and replacement value for SERIES as value.

    Returns:
    pd.DataFrame: The modified DataFrame.
    """
    # Replace the SERIES values based on the symbol_replacements dictionary
    df[' SERIES'] = df['SYMBOL'].map(symbol_replacements).fillna(df[' SERIES'])

    return df


def calculate_volume_increment_stock(df1, df2):
    # Merge the two dataframes on Index Name
    merged_df = pd.merge(df1, df2, on='SYMBOL', suffixes=('_df1', '_df2'))

    # Calculate the volume increment for each Index Name
    merged_df['Volume Increment'] = round(
        merged_df[' DELIV_QTY_df2'].astype(int) / merged_df[' DELIV_QTY_df1'].astype(int), 2)
    merged_df['Change % Previous'] = round((((merged_df[' CLOSE_PRICE_df1'].astype(float) - merged_df[' PREV_CLOSE_df1'].astype(
        float)) / merged_df[' PREV_CLOSE_df1'].astype(float)) * 100), 2)
    merged_df['Change % Current'] = round((((merged_df[' CLOSE_PRICE_df2'].astype(float) - merged_df[' PREV_CLOSE_df2'].astype(float)) / merged_df[' PREV_CLOSE_df2'].astype(float)) * 100),2)

    return merged_df[['SYMBOL', ' SERIES_df2', 'Change % Previous','Change % Current','Volume Increment']]