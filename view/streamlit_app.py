import sys
import os
# Add root directory to sys.path for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from model import data_processing as dp
from view import visualization as vz


DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'supermarket_sales.csv')

def main():
    st.title("Supermarket Sales Analysis")

    # Load and clean data
    data = dp.load_data(DATA_FILE)
    clean_data = dp.clean_data(data)
    st.write(f"Data cleaned: Removed {len(data) - len(clean_data)} invalid rows")
    
    # Show total sales
    total = dp.total_sales(clean_data)
    st.subheader(f"Total Sales: ${total:,.2f}")

    # Sidebar filters
    options = ["Sales by Product Line", "Sales by City"]
    choice = st.sidebar.selectbox("Select visualization", options)

    if choice == "Sales by Product Line":
        product_lines, sales = dp.sales_by_product_line(clean_data)
        plt = vz.plot_bar(product_lines, sales, "Sales by Product Line", "Product Line", "Sales ($)")
        st.pyplot(plt)

    elif choice == "Sales by City":
        cities, sales = dp.sales_by_city(clean_data)
        plt = vz.plot_bar(cities, sales, "Sales by City", "City", "Sales ($)")
        st.pyplot(plt)

if __name__ == '__main__':
    main()
