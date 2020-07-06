import pandas as pd

# analysis functions

def analyze(df):
    df['Quantity'] = 1
    final_df = df[['country', 'title', 'gender', 'Quantity']].groupby(['country', 'title', 'gender'], as_index=False).count()
    final_df['Percentage'] = (final_df['Quantity'] / final_df['Quantity'].sum() * 100).round(2).astype(str) + '%'
    final_df.sort_values(by='Quantity', ascending=False, inplace=True)
    return final_df


def filter_country(countr,df):
    if countr == "":
        return df
    else:
        return df[df["country"]==countr]