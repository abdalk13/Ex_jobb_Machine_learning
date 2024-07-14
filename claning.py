import pandas as pd

data = pd.read_excel('data1.xlsx')
print (data.columns)

summed_data = pd.DataFrame(columns=data.columns)
for value1 in data.iloc[:, 0].unique():
    for value3 in data.iloc[:, 2].unique():
        matching_rows = data[(data.iloc[:, 0] == value1) & (data.iloc[:, 2] == value3)]
        if len(matching_rows) > 0:
            summed_value = matching_rows.iloc[:, -1].sum()
            summed_value0 = ','.join(matching_rows.iloc[:, -2].astype(str))  
            summed_data.loc[len(summed_data)] = matching_rows.iloc[0]            
            summed_data.iloc[-1, -1] = summed_value  

summed_data.to_excel('24_m.xlsx', index=False)
data = pd.read_excel('24_mkolumn.xlsx')

filtered_data = data[data['not allowed to show'].str.contains('not allowed to show', case=False)]

filtered_data.to_excel('24_mkolumn_bara_diseloel.xlsx', index=False)


# Läs in din data från filen
data = pd.read_excel('24_m.xlsx')

omstrukturerad_data = []

# Loopa igenom varje unik "not allowed to show"
# for equi_nummer in data['not allowed to show'].unique():
    # Skapa nya kolumner för m1 och m2 för den aktuella "not allowed to show"
   # m1_pris = None
   # m2_pris = None
   # for index, row in data[data['not allowed to show'] == equi_nummer].iterrows():
   #     if row['per'] == 2021:
     #       m1_pris = row['1']
     #   elif row['per'] == 2022:
     #       m2_pris = row['2']
    #omstrukturerad_data.append({'not allowed to show': equi_nummer, 'm1': m1_pris, 'm2': m2_pris})

omstrukturerad_data = []
for equi_nummer in data['not allowed to show'].unique():
        m1_pris, m2_pris, m3_pris, m4_pris, m5_pris, m6_pris, m7_pris, m8_pris, m9_pris, m10_pris, m11_pris, m12_pris, m13_pris, m14_pris, m15_pris, m16_pris, m17_pris, m18_pris, m19_pris, m20_pris, m21_pris, m22_pris, m23_pris, m24_pris = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
        for index, row in data[data['not allowed to show'] == equi_nummer].iterrows(): 
            if row['per'] == 1.2021:
                m1_pris = row['pr']
            elif row['per'] == 2.2021:
                m2_pris = row['pr']
            elif row['per'] == 3.2021:
                m3_pris = row['pr']
            elif row['per'] == 4.2021:
                m4_pris = row['pr']
            elif row['per'] == 5.2021:
                m5_pris = row['pr']
            elif row['per'] == 6.2021:
                m6_pris = row['pr']
            elif row['per'] == 7.2021:
                m7_pris = row['pr']
            elif row['per'] == 8.2021:
                m8_pris = row['pr']
            elif row['per'] == 9.2021:
                m9_pris = row['pr']
            elif row['per'] == 10.2021:
                m10_pris = row['pr']
            elif row['per'] == 11.2021:
                m11_pris = row['pr']
            elif row['per'] == 12.2021:
                m12_pris = row['pr']
            elif row['per'] == 1.2022:
                m13_pris = row['pr']
            elif row['per'] == 2.2022:
                m14_pris = row['pr']
            elif row['per'] == 3.2022:
                m15_pris = row['pr']
            elif row['per'] == 4.2022:
                m16_pris = row['pr']
            elif row['per'] == 5.2022:
                m17_pris = row['pr']
            elif row['per'] == 6.2022:
                m18_pris = row['pr']
            elif row['per'] == 7.2022:
                m19_pris = row['pr']
            elif row['per'] == 8.2022:
                m20_pris = row['pr']
            elif row['per'] == 9.2022:
                m21_pris = row['pr']
            elif row['per'] == 10.2022:
                m22_pris = row['pr']
            elif row['per'] == 11.2022:
                m23_pris = row['pr']
            elif row['per'] == 12.2022:
                m24_pris = row['pr']
            omstrukturerad_data.append({'not allowed to show': equi_nummer, 
                        'm1': m1_pris, 'm2': m2_pris, 'm3': m3_pris, 'm4': m4_pris, 
                        'm5': m5_pris, 'm6': m6_pris, 'm7': m7_pris, 'm8': m8_pris, 
                        'm9': m9_pris, 'm10': m10_pris, 'm11': m11_pris, 'm12': m12_pris,
                        'm13': m13_pris, 'm14': m14_pris, 'm15': m15_pris, 'm16': m16_pris, 
                        'm17': m17_pris, 'm18': m18_pris, 'm19': m19_pris, 'm20': m20_pris, 
                        'm21': m21_pris, 'm22': m22_pris, 'm23': m23_pris, 'm24': m24_pris})

omstrukturerad_dataframe = pd.DataFrame(omstrukturerad_data)

omstrukturerad_dataframe.drop_duplicates(subset=['not allowed to show'], keep='last', inplace=True)
kombinerad_data = pd.merge(data, omstrukturerad_dataframe, on='not allowed to show', how='left')
kombinerad_data.drop(columns=['not allowed to show'], inplace=True)

kombinerad_data.to_excel('24_mkolumn.xlsx', index=False)

# Read the Excel file
data = pd.read_excel('24_mkolumn.xlsx')

data_filled = data.fillna(0)

data_filled.to_excel('24_mkolumn.xlsx', index=False)  
data = pd.read_excel('24_mkolumn_bara_diseloel.xlsx')

def handle_negative(value):
    if value < 0:
        return 0
    else:
        return value
for col_idx in range(9, 33):
    data.iloc[:, col_idx] = data.iloc[:, col_idx].apply(handle_negative)
data.to_excel('24_mkolumn_bara_diseloel_utanminus.xlsx', index=False)
