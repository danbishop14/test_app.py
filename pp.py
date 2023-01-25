import pandas as pd

URL = "https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_market_tracker/zip_code_market_tracker.tsv000.gz"

def split_df_to_parquet(df, output_dir):
    # Group the DataFrame by state_code
    grouped = df.groupby('state_code')

    # Iterate over each group and write to a separate Parquet file
    for state_code, group in grouped:
        group.to_parquet(f'{output_dir}/{state_code}.parquet')
        group.to_csv(f'{output_dir}/{state_code}.csv')

# Example usage
df = pd.read_csv('URL',sep = '\t')

# df = df.head()
# df.to_csv('test.csv')

print(df.head())
print(df.columns)
split_df_to_parquet(df, 'output_parquet_files')
