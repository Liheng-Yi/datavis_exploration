import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have the data frame df already loaded with the correct data
data = {
    'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'pop': [37253956, 37638369, 37948800, 38260787, 38596972, 38918045, 39167117, 39358497, 39461588, 39512223],
    'white_pop': [27636403, 27831691, 27987654, 28130737, 28280234, 28404773, 28484043, 28518935, 28497432, 28424739],
    'black_pop': [2486549, 2495664, 2504171, 2509919, 2522246, 2531244, 2537131, 2543564, 2547988, 2552757],
    'asian_pop': [5038123, 5170412, 5278438, 5403085, 5537896, 5685743, 5813827, 5930737, 6021008, 6110945],
    'indian_pop': [622107, 625990, 629071, 631894, 635115, 638274, 641036, 643442, 646626, 649862]
}
df = pd.DataFrame(data)

# Calculate the percentage change for each demographic category
df['pop_pct_change'] = df['pop'].pct_change() * 100
df['white_pop_pct_change'] = df['white_pop'].pct_change() * 100
df['black_pop_pct_change'] = df['black_pop'].pct_change() * 100
df['asian_pop_pct_change'] = df['asian_pop'].pct_change() * 100
df['indian_pop_pct_change'] = df['indian_pop'].pct_change() * 100

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(df['year'], df['pop_pct_change'], label='Total Population Change (%)', marker='o', linewidth=2)
plt.plot(df['year'], df['white_pop_pct_change'], label='White Population Change (%)', marker='o', linewidth=2)
plt.plot(df['year'], df['black_pop_pct_change'], label='Black Population Change (%)', marker='o', linewidth=2)
plt.plot(df['year'], df['asian_pop_pct_change'], label='Asian Population Change (%)', marker='o', linewidth=2)
plt.plot(df['year'], df['indian_pop_pct_change'], label='American Indian Population Change (%)', marker='o', linewidth=2)

plt.title('Yearly Percentage Change in Population Demographics in California (2010-2019)')
plt.xlabel('Year')
plt.ylabel('Percentage Change')
plt.grid(True)
plt.legend()
plt.show()
