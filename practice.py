# print("Hello World Manchester
# Swindon
# Sunder
# Derby
# Gloucester
# Luton
# Dundee
# Kingston upon Hull
# Nottingom
# Blackpool
# Cannock
# Canterbury
# Sheffield
# London
# Bristol
# Bradford
# Birmingham
# Bolton
# Preston
# Glasgow
# ")


# import pandas as pd
# import numpy as np

# 1. Assume 'df' is your large DataFrame (30000 rows)
# df = pd.read_csv('your_data_file.csv')

# # The list of cities you provided:
# cities = [
#     "Manchester", "Swindon", "Sunderland", "Derby", "Gloucester",
#     "Luton", "Dundee", "Kingston upon Hull", "Nottingham", "Blackpool",
#     "Cannock", "Canterbury", "Sheffield", "London", "Bristol",
#     "Bradford", "Birmingham", "Bolton", "Preston", "Glasgow"
# ]

# # The corresponding coordinates as a dictionary for easy mapping
# coordinates = {
#     "Manchester": (53.4790, -2.2452), "Swindon": (51.56, -1.78),
#     "Sunderland": (54.906, -1.381), "Derby": (52.9247, -1.4780),
#     "Gloucester": (51.8667, -2.2500), "Luton": (51.8783, -0.4147),
#     "Dundee": (56.4620, -2.9707), "Kingston upon Hull": (53.7431, -0.3344),
#     "Nottingham": (52.9561, -1.1512), "Blackpool": (53.8142, -3.0503),
#     "Cannock": (52.6953, -1.9723), "Canterbury": (51.2780, 1.0802),
#     "Sheffield": (53.3811, -1.4701), "London": (51.5072, -0.1275),
#     "Bristol": (51.4536, -2.5975), "Bradford": (53.8000, -1.7500),
#     "Birmingham": (52.4800, -1.9025), "Bolton": (53.5796, -2.4287),
#     "Preston": (53.7632, -2.7040), "Glasgow": (55.8642, -4.2518)
# }

# # 3. Add random cities column first
# df['City'] = np.random.choice(cities, size=len(df), replace=True)

# # 4. Use the pandas .map() function to look up the coordinates for each random city
# df['Latitude'] = df['City'].map(lambda x: coordinates[x][0])
# df['Longitude'] = df['City'].map(lambda x: coordinates[x][1])

# # Display the result
# print(df.head())

#Read Excel File
import pandas as pd
import numpy as np
df= pd.read_excel('data/Grade.xlsx')

# print("Hello World")
# cities = [
#     "Manchester", "Swindon", "Sunderland", "Derby", "Gloucester",
#     "Luton", "Dundee", "Kingston upon Hull", "Nottingham", "Blackpool",
#     "Cannock", "Canterbury", "Sheffield", "London", "Bristol",
#     "Bradford", "Birmingham", "Bolton", "Preston", "Glasgow"
# ]

# df['Trade_City'] = np.random.choice(cities, size=len(df), replace=True)
# print(df.head())

# output_file_name = 'data/vehicle_grade.csv'
# df.to_csv(output_file_name, index=False)

# print(f"Successfully saved updated data to {output_file_name}")
# print(df.columns)


# 1. Create a dummy DataFrame with 30,000 rows for demonstration
# # Replace this line with your actual DataFrame loading code:
# df = pd.DataFrame(np.random.randint(0, 100, size=(30000, 1)), columns=['Dummy_Data'])
# print(f"Original DataFrame shape: {df.shape}")

# 2. Define the cities list and the county mapping dictionary
cities = [
    "Manchester", "Swindon", "Sunderland", "Derby", "Gloucester",
    "Luton", "Dundee", "Kingston upon Hull", "Nottingham", "Blackpool",
    "Cannock", "Canterbury", "Sheffield", "London", "Bristol",
    "Bradford", "Birmingham", "Bolton", "Preston", "Glasgow"
]

county_map = {
    "Manchester": "Greater Manchester", "Swindon": "Wiltshire", "Sunderland": "Tyne and Wear",
    "Derby": "Derbyshire", "Gloucester": "Gloucestershire", "Luton": "Bedfordshire",
    "Dundee": "Angus (Council Area)", "Kingston upon Hull": "East Riding of Yorkshire",
    "Nottingham": "Nottinghamshire", "Blackpool": "Lancashire", "Cannock": "Staffordshire",
    "Canterbury": "Kent", "Sheffield": "South Yorkshire", "London": "Greater London",
    "Bristol": "Bristol (Unitary Authority)", "Bradford": "West Yorkshire",
    "Birmingham": "West Midlands", "Bolton": "Greater Manchester", "Preston": "Lancashire",
    "Glasgow": "Glasgow (Council Area)"
}

# 3. Add the 'City' column with random selections (with replacement)
df['City'] = np.random.choice(cities, size=len(df), replace=True)

# 4. Use the .map() function to look up the corresponding 'County' for each city
df['County'] = df['City'].map(county_map)

# Assuming you chose 'Standard' as the replacement word
df['Category'] = df['Category'].replace('Select', 'Standard')
# 5. Display the results
print("\nDataFrame with new columns added:")
print(df.head())
print(f"\nDataFrame shape after additions: {df.shape}")

output_file_name = 'data/vehicle_grade.csv'
df.to_csv(output_file_name, index=False)  