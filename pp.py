import pandas as pd

URL = "https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_market_tracker/zip_code_market_tracker.tsv000.gz"

def split_df_to_parquet(df, output_dir):
    # Group the DataFrame by state_code
    df = df.loc[df['property_type'] == 'Single Family Residential'].assign(period_end = pd.to_datetime(df['period_end']),zipcode = df['region'].str.replace('Zip Code:',''))
    grouped = df.groupby('state_code')

    # Iterate over each group and write to a separate Parquet file
    for state_code, group in grouped:
        group.to_parquet(f'{output_dir}/{state_code}.parquet')
        # group.to_csv(f'{output_dir}/{state_code}.csv')

# Example usage
df = pd.read_csv(URL,sep = '\t')


# df.to_csv('test.csv')

split_df_to_parquet(df, 'output_parquet_files')
