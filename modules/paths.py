import os


def get_desktop_path():
    # Get the user's home directory
    home = os.path.expanduser("~")
    # Construct the path to the Desktop
    desktop = os.path.join(home, 'Desktop')
    return desktop


def get_data_path():
    desktop = get_desktop_path()
    # Construct the path to the data folder on the Desktop
    data_path = os.path.join(desktop, 'data')
    return data_path


def get_nifty_path():
    data_path = get_data_path()
    # Construct the path to the nifty folder inside the data folder
    nifty_path = os.path.join(data_path, 'broad')
    return nifty_path


def get_ind_nifty50list_csv_path():
    nifty_path = get_nifty_path()
    # Construct the path to the ind_nifty50list.csv file inside the nifty folder
    ind_nifty50list_csv_path = os.path.join(nifty_path, 'ind_nifty50list.csv')
    return ind_nifty50list_csv_path


def get_ind_niftynext50list_csv_path():
    nifty_path = get_nifty_path()
    # Construct the path to the ind_nifty50list.csv file inside the nifty folder
    ind_niftynext50list_csv_path = os.path.join(nifty_path, 'ind_niftynext50list.csv')
    return ind_niftynext50list_csv_path


def get_indice_path():
    data_path = get_data_path()
    # Construct the path to the indice folder inside the data folder
    indice_path = os.path.join(data_path, 'indice')
    return indice_path


def get_indice_csv_path(user_date: str):
    indice_path = get_indice_path()
    # Construct the path to the ind_close_all_date inside the indice folder
    indice_csv_path = os.path.join(indice_path, f'ind_close_all_{user_date}.csv')
    return indice_csv_path


def get_stock_path():
    data_path = get_data_path()
    # Construct the path to the stock folder inside the data folder
    stock_path = os.path.join(data_path, 'stock')
    return stock_path


def get_stock_csv_path(user_date: str):
    stock_path = get_stock_path()
    # Construct the path to the ind_close_all_date inside the stock folder
    stock_csv_path = os.path.join(stock_path, f'sec_bhavdata_full_{user_date}.csv')
    return stock_csv_path


def get_output_path():
    data_path = get_data_path()
    # Construct the path to the stock folder inside the data folder
    output_path = os.path.join(data_path, 'output')
    return output_path