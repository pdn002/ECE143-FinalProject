#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:21:04 2024

@author: macbookpro2013
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def source_quantity_units(file_path):
    with open(file_path, 'r') as file:

        csv_reader = csv.DictReader(file)

        cleaned_data = []

        #if there are any missing values or if quantity is 0 do not include
        for row in csv_reader: 
            if row['Source'] and row['Quantity'] and row['Units']:           
                if float(row['Quantity']) != 0:               
                    cleaned_data.append(row)


        #removing any duplicates in the data, only unique values
        cleaned_data = [dict(t) for t in {tuple(d.items()) for d in cleaned_data}]

        cleaned_data = pd.DataFrame(cleaned_data)

        #using numeric to be able to add the quantity values
        cleaned_data['Quantity'] = pd.to_numeric(cleaned_data['Quantity'])

        # group if source and units are the same and then add all the quantities together
        summ = cleaned_data.groupby(['Source', 'Units']).agg({'Quantity': 'sum'}).reset_index()

    #making graphs by respective units
    gallons = summ[summ['Units'] == 'Gallons']

    plt.figure(figsize=(10, 6))
    plt.bar(gallons['Source'], gallons['Quantity'], color='skyblue')
    plt.xlabel('Source')
    plt.ylabel('Quantity (Gallons)')
    plt.title('Quantity of Oil Spills by Source')
    plt.xticks(rotation=45, ha='right')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.0f}M'.format(x / 1e6)))
    plt.tight_layout()
    plt.show()

    pounds = summ[summ['Units'] == 'Pounds']

    plt.figure(figsize=(10, 6))
    plt.bar(pounds['Source'], pounds['Quantity'], color='lightgreen')
    plt.xlabel('Source')
    plt.ylabel('Quantity (Pounds)')
    plt.title('Quantity of Oil Spills by Source')
    plt.xticks(rotation=45, ha='right')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.0f}M'.format(x / 1e6))) 
    plt.tight_layout()
    plt.show()

    return summ