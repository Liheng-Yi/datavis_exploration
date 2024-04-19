import pandas as pd


dataset_path = './US_county_census_est_race_eth_2010_2019.csv'
df = pd.read_csv(dataset_path)

# Filter states
states_to_keep = ["California", "Oregon", "Florida", "Washington", "Texas"]
filtered_df = df[df['state'].isin(states_to_keep)]


required_columns = ["state", "year", "pop", "white_pop", "black_pop",
                    "asian_pop", "indian_pop", "pacific_pop", "two_pop",
                    "not_hisp_pop", "hisp_pop"]
filtered_df = filtered_df[required_columns]

columns_to_sum = ['pop', 'white_pop', 'black_pop', 'asian_pop', 'indian_pop', 'pacific_pop', 'two_pop', 'not_hisp_pop', 'hisp_pop']

# Group by 
aggregated_df = filtered_df.groupby([ 'state','year'])[columns_to_sum].sum()


aggregated_df.to_csv('filtered_data.csv', index=False)
