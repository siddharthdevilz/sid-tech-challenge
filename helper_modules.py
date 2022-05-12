import pandas as pd
import json
import sys
from os.path import exists
import logging

log = logging.getLogger(__name__)

def open_file(filepath):
    ## Verify file type
    if filepath.lower().endswith('.json'):

        ## Verify file exists
        if exists(filepath):
            return open(filepath)
        else:
            log.error("The file does not exist !!")
            sys.exit(1)
    
    else:
        log.error("File is wrong format !!")
        sys.exit(1)

def load_data(file):
    ## Load the data from the file into dataframe
    try:
        data = json.load(file)
        df = pd.json_normalize(data, record_path=['items'], meta=['brand', 'customer_id', 'purchase_id'],errors='ignore')
        return df
    except:
        log.error("There was an error loading data from the file !!")
        sys.exit()


def transform_data(df, mandatory):

    ## Convert numeric columns to numeric data type, and remove garbage values
    df['price']=pd.to_numeric(df['price'], errors='coerce')
    df['quantity']=pd.to_numeric(df['quantity'], errors='coerce')

    ## Move records with missing mandatory fields to error table
    df_error = df[df[mandatory].isna().any(1)]
    df=df.dropna(subset=mandatory)

    ## Create product table
    df_product = df[['product_name', 'brand', 'department', 'product_category']]

    ## Create PO table and add 'total_price'
    df = df.assign(total_price = df['price'] * df['quantity'])
    df_po = df[['purchase_id', 'customer_id', 'product_name', 'price', 'quantity', 'total_price']]

    ## Create PO_total table to hold total purchase amount for each PO
    df_pos_total = df_po.groupby('purchase_id', as_index=False)['total_price'].sum()

    return [df, df_product, df_po, df_pos_total, df_error]


