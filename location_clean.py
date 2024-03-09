import pandas as pd

def location_clean(data):
    '''
    cleans out data to only include relevant location columns
    
    args:
        data (pd.DataFrame)
    '''
    assert isinstance(data, pd.DataFrame)

    # get rid of unnecessary columns and change units to all be gallons
    location_data = data.loc[:, ['Locality', 'County', 'Quantity', 'Units']].copy()
    location_data.loc[location_data['Units'] == 'Pounds', 'Quantity'] = location_data.loc[location_data['Units'] == 'Pounds', 'Quantity'] / 7.21
    location_data.loc[location_data['Units'] == 'Pounds', ['Units']] = 'Gallons'

    return location_data.sort_values(['Quantity'], ascending=False)