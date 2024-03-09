import pandas as pd

def total_spill_location(location_data):
    '''
    gets total oil spilled by locatlity and county
    
    args:
        location_data (pd.DataFrame): data with relevent columns about quantity spilled and location
    '''
    assert isinstance(location_data, pd.DataFrame)

    # get total oil spilled by each locality and county
    location_total = location_data.copy()
    location_total['Total Spilled'] = location_total.groupby(['Locality', 'County'])['Quantity'].transform('sum')
    location_total = location_total.drop(['Quantity', 'Units'], axis='columns')
    location_total = location_total.drop_duplicates(subset=['Locality', 'County'])

    # clean up total spilled by droping NaN values, sorting, and renaming column
    location_total = location_total.dropna(subset=['Total Spilled'])
    location_total = location_total.sort_values(['Total Spilled'], ascending=False)
    location_total = location_total.rename(columns={'Total Spilled': 'Total Spilled (Gallons)'})
    location_total = location_total.reset_index()
    location_total = location_total.drop(['index'], axis='columns')

    return location_total