import pandas as pd

def location_freq(location_data):
    ''' 
    counts the frequency of spills by location
    
    args:
        location_data (pd.DataFrame): the data to get frequency from
    '''
    assert isinstance(location_data, pd.DataFrame)

    location_freq = pd.DataFrame(location_data[['Locality', 'County']].value_counts())
    location_freq = location_freq.reset_index()
    return location_freq
