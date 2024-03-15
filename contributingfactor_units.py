import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('./Spill_Incidents.csv')
data['Contributing Factor'] = data['Contributing Factor'].replace(['Other'], 'Unknown')
clean_data = data.dropna(subset=['Units']).copy()
clean_data = clean_data[~clean_data['Contributing Factor'].isin(['Unknown'])]

top_factors_count = clean_data['Contributing Factor'].value_counts().head(5)
plt.figure(figsize=(8, 8))
top_factors_count.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Contributing Factors')
plt.ylabel('')
plt.tight_layout()
plt.show()

top_factors = top_factors_count.index
filtered_data = clean_data[(clean_data['Contributing Factor'].isin(top_factors)) & (clean_data['Units'] == 'Gallons')]
average_quantities = filtered_data.groupby('Contributing Factor')['Quantity'].mean().reset_index()
average_quantities = average_quantities.sort_values(by='Quantity', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(average_quantities['Contributing Factor'], average_quantities['Quantity'], color='skyblue')
plt.title('Top Average Quantity per Case')
plt.title('Top Average Quantity per Case')
plt.xlabel('Average Quantity in Gallons')
plt.ylabel('Contributing Factor')
plt.tight_layout()
plt.show()

data['Spill Date'] = pd.to_datetime(data['Spill Date'], errors='coerce')
min_year = data['Spill Date'].dt.year.min()
max_year = data['Spill Date'].dt.year.max()
print(f"Start Year: {min_year}, End Year: {max_year}")