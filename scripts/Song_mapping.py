import pandas as pd

# Load the dataset
file_path = "data\rolling_stones_spotify.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Generate mapping if 'name' column is encoded
if df['name'].dtype != 'O':  # If 'name' is numeric (encoded)
    name_mapping = pd.DataFrame({"encoded_name": df['name'], "name": df['name'].astype(str)})
    name_mapping.to_csv("data/song_name_mapping.csv", index=False)

print("Song name mapping file created successfully!")
