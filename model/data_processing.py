#model/: Contains code for data cleaning and processing.
import numpy as np

def load_data(file_path):
    # Load CSV as structured numpy array
    data = np.genfromtxt(file_path, delimiter=',', dtype=None, encoding='utf-8', names=True)
    return data

def clean_data(data):
    # Remove rows with empty Invoice_ID, empty Branch or zero Unit_price
    valid_mask = (data['Invoice_ID'] != '') & (data['Branch'] != '') & (data['Unit_price'] > 0)
    clean_data = data[valid_mask]
    return clean_data

def total_sales(data):
    # Calculate total sales sum
    return np.sum(data['Total'])

def sales_by_product_line(data):
    # Unique product lines
    product_lines = np.unique(data['Product_line'])
    # Sum total sales by product line
    sales = []
    for p in product_lines:
        mask = (data['Product_line'] == p)
        sales.append(np.sum(data['Total'][mask]))
    return product_lines, sales

def sales_by_city(data):
    city_names = np.unique(data['City'])
    sales = []
    for c in city_names:
        mask = (data['City'] == c)
        sales.append(np.sum(data['Total'][mask]))
    return city_names, sales
