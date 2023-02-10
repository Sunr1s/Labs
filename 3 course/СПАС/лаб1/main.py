 
import random
import pandas as pd
import matplotlib.pyplot as plt

# Define the number of data points you want to generate
num_data_points = 1000

# Define the possible cities
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

# Generate the random data
data = []
for i in range(num_data_points):
    city_1 = random.choice(cities)
    city_2 = random.choice(cities)
    while city_1 == city_2:
        city_2 = random.choice(cities)
    distance = random.randint(100, 5000)
    time = distance / random.uniform(40, 120)
    cost = distance / random.uniform(0.05, 0.15)
    data.append([city_1, city_2, distance, time, cost])

# Create the Pandas DataFrame
df = pd.DataFrame(data, columns=['City 1', 'City 2', 'Distance', 'Time', 'Cost'])

# Write the DataFrame to a csv file
df.to_csv('modified_table.csv', index=False)

# Write the DataFrame to an xlsx file
df.to_excel('modified_table.xlsx', index=False)

# Write the DataFrame to an html file
df.to_html('modified_table.html', index=False)


print(df.groupby('City 1').mean())

# Scatter plot of distance vs. time
plt.scatter(df['Distance'], df['Time'])
plt.xlabel('Distance (km)')
plt.ylabel('Time (hr)')
plt.title('Relationship between Distance and Time')
plt.show()

# Scatter plot of distance vs. cost
plt.scatter(df['Distance'], df['Cost'])
plt.xlabel('Distance (km)')
plt.ylabel('Cost ($)')
plt.title('Relationship between Distance and Cost')
plt.show()