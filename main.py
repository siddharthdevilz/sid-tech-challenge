import helper_modules as hp
import logging
import sys
import json

## Setup logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

if __name__=="__main__":
    ## Check if file argument is provided
    if len(sys.argv)>1:

        ## Open file
        f = hp.open_file(sys.argv[1])

        ## Load data from file
        df_original = hp.load_data(f)

        ## Define mandatory fields - if these fields are absent, record is invalid
        mandatory = ['purchase_id', 'customer_id', 'price', 'quantity', 'product_name']

        ## Transform the data
        df, df_product, df_po, df_pos_total, df_error = hp.transform_data(df_original, mandatory)

        ## Calculate the required output
        output = {}
        output['Total volume of spend '] = df_pos_total['total_price'].sum()
        output['Average purchase value'] = df_pos_total['total_price'].mean()
        output['Maximum purchase value'] = df_pos_total['total_price'].max()
        output['Median purchase value'] = df_pos_total['total_price'].median()
        output['Number of unique products purchased'] = df_po['product_name'].nunique()
        json_data = json.dumps(output)
        print(json_data)

    else:
        log.error("Pleae provide file name as argument !!")