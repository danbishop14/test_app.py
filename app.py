import streamlit as st
import pandas as pd


def display_parquet(state_code):
    df = pd.read_parquet(f'output_parquet_files/{state_code}.parquet')
    st.dataframe(df)

st.title('Parquet File Viewer')


state_codes = ['AL', 'AK', 'AZ', 'AR', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
# state_codes = ['AK','AL','AR','AZ']

state_code = st.selectbox('Select a State', state_codes)

display_parquet(state_code)
