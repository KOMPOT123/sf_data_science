import pandas as pd

def get_weekend(weekday):
    if weekday == 'Saturday' or weekday == 'Sunday':
        return 1
    else:
        return 0
    
    
melb_data = pd.read_csv('C:/Users/studo/Documents/skill/sf_data_science/panda/melb_data_ps/melb_data_ps.csv', sep=',')
melb_df = melb_data.copy()
sub_top = melb_df['Suburb'].value_counts().nlargest(119).index
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in sub_top else 'other')
melb_df['Suburb'] = melb_df['Suburb'].astype('category')

print(melb_df.info())

'''melb_df['Date'] = pd.to_datetime(melb_df['Date'])
melb_df['WeekdaySale'] = melb_df['Date'].dt.day_name()
melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
mask1 = melb_df['Weekend'] == 1
print(round(melb_df[mask1]['Price'].mean(), 2))'''
'''
weekend_count = melb_df[(melb_df['WeekdaySale'] == 'Saturday') | (melb_df['WeekdaySale'] == 'Sunday')].count()
print(weekend_count)
'''
'''
df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')
df['Time'] = pd.to_datetime(df.Time)
df['Date'] = df['Time'].dt.date
print(df[df['State']=='NV']['Date'].diff().dt.days.mean())
'''