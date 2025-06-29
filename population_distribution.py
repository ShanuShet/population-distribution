#population_distribution.py
import pandas as pd
import matplotlib.pyplot as plt
import zipfile

# Path to the zip file and the CSV inside it
zip_path = r'C:\Users\priya\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_119973.zip'
csv_filename = 'API_SP.POP.TOTL_DS2_en_csv_v2_119973.csv'

# Open the zip file and read the CSV file inside
with zipfile.ZipFile(zip_path) as z:
    with z.open(csv_filename) as f:
        df = pd.read_csv(f, skiprows=4)

# Filter for India
india = df[df['Country Name'] == 'India']

# Extract years and population values (last 30 years for clarity)
years = [str(y) for y in range(1993, 2023)]
population = india[years].values.flatten()

# Plot bar chart of population by year
plt.figure(figsize=(12, 6))
plt.bar(years, population, color='deepskyblue')
plt.title("India's Total Population (1993-2022)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Age groups and their populations (in millions)
age_groups = ['0-20', '21-64', '65+']
populations = [512, 807, 98]

plt.figure(figsize=(8, 6))
bars = plt.bar(age_groups, populations, color=['gold', 'deepskyblue', 'hotpink'])

# Add value labels on top of bars
for bar, pop in zip(bars, populations):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
             f'{pop} Mn', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.title("India's Population Distribution by Age Group (2022)", fontsize=15, fontweight='bold')
plt.xlabel("Age Group")
plt.ylabel("Population (Millions)")
plt.ylim(0, max(populations) + 100)  # Adjusted for better visualisation
plt.tight_layout()
plt.show()