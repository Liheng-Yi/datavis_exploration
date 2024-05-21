
nodes_data = {
    "Id": [1, 2, 3, 4, 5],
    "Label": ["African American/Black", "American Indian/Alaska Native", "Asian", "Hispanic/Latino", "White"],
    "Highschool_Grad_Percent": [72.5, 73.0, 94.1, 80.5, 88.2],
    "Income": [61740, 67230, 116060, 71120, 102540]
}
nodes_df = pd.DataFrame(nodes_data)

# Edges Data (creating a fully connected network for simplicity)
edges_data = {
    "Source": [1, 1, 1, 1, 2, 2, 2, 3, 3, 4],
    "Target": [2, 3, 4, 5, 3, 4, 5, 4, 5, 5],
    "Weight": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}
edges_df = pd.DataFrame(edges_data)

# Save DataFrames to CSV
nodes_csv_path = "./odes.csv"
edges_csv_path = "./edges.csv"
nodes_df.to_csv(nodes_csv_path, index=False)
edges_df.to_csv(edges_csv_path, index=False)

nodes_csv_path, edges_csv_path
