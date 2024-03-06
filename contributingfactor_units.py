import pandas as pd
import matplotlib.pyplot as plt

file_path = './Spill_Incidents.csv'
data = pd.read_csv(file_path)

# Data Cleaning and Modification
# Remove records with missing 'Units'
clean_data = data.dropna(subset=['Units']).copy()

# Combine "Unknown" and "Other" into "Unknown"
clean_data['Contributing Factor'] = clean_data['Contributing Factor'].replace(['Other'], 'Unknown')

# compute sum and average
data_cleaned = clean_data.groupby(['Contributing Factor', 'Units'])['Quantity'].sum().reset_index()
avg_data_cleaned = clean_data.groupby(['Contributing Factor', 'Units'])['Quantity'].mean().reset_index()

# Filter data for gallons only
gallons_data_cleaned = data_cleaned[data_cleaned['Units'] == 'Gallons']
gallons_average_data_cleaned = avg_data_cleaned[avg_data_cleaned['Units'] == 'Gallons']

# create plots for total quantities
def create_plot(data, title_prefix='Top'):
    data_sorted = data.sort_values(by='Quantity', ascending=False).head(10)  # Show top 10 
    factors = data_sorted['Contributing Factor']
    quantities = data_sorted['Quantity']
    
    plt.figure(figsize=(10, 6))
    plt.barh(factors, quantities, color='red')
    plt.xlabel('Quantity in Gallons')
    plt.ylabel('Contributing Factor')
    plt.title(f'{title_prefix} Contributing Factors by Total Quantity in Gallons')
    plt.tight_layout()
    plt.show()

def create_average_plot(data):
    data_sorted = data.sort_values(by='Quantity', ascending=False).head(10)  # Show top 10 
    factors = data_sorted['Contributing Factor']
    averages = data_sorted['Quantity']
    
    plt.figure(figsize=(10, 6))
    plt.barh(factors, averages, color='red')
    plt.xlabel('Average Quantity in Gallons')
    plt.ylabel('Contributing Factor')
    plt.title('Top Contributing Factors by Average Quantity in Gallons')
    plt.tight_layout()
    plt.show()


create_plot(gallons_data_cleaned)
create_average_plot(gallons_average_data_cleaned)
