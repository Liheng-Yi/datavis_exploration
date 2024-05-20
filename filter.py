import pandas as pd

# Load dataset
dataset_path = './US_county_census_est_race_eth_2010_2019.csv'
df = pd.read_csv(dataset_path)

# Filter states
states_to_keep = ["California", "Oregon", "Florida", "Washington", "Texas"]
filtered_df = df[df['state'].isin(states_to_keep)]

# Specify required columns
required_columns = [
    "state", "year", "pop", "white_pop", "black_pop",
    "asian_pop", "indian_pop", "pacific_pop", "two_pop",
    "not_hisp_pop", "hisp_pop"
]
filtered_df = filtered_df[required_columns]

# Columns to aggregate by sum
columns_to_sum = [
    'pop', 'white_pop', 'black_pop', 'asian_pop', 'indian_pop', 
    'not_hisp_pop', 'hisp_pop'
]

# Group by state and year, then sum
aggregated_df = filtered_df.groupby(['state', 'year'])[columns_to_sum].sum()

# Save aggregated data to CSV, keeping the index
aggregated_df.to_csv('filtered_data.csv', index=True)
