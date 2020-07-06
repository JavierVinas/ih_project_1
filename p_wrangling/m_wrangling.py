import pandas as pd

# wrangling functions

# Clean data from gender column to reflect only two values: Male and Female

def wrangle(df):
    print('Cleaning up the gender column...')
    df["gender"].replace(to_replace=['male', 'Fem', 'FeMale', 'female'],
                                       value=['Male', 'Female', 'Female', 'Female'], inplace=True)
    return df


# Merge all dataframes into

def merge_dfs(country_info,career_info,clean_gender,job_titles, country_names):
    df_1 = pd.merge(country_info, career_info, how='inner', on='uuid')
    df_2 = pd.merge(df_1, clean_gender, how = 'inner', on = 'uuid')
    df_2 = df_2[['uuid', 'country_code', 'normalized_job_code', 'gender']]
    df_3 = pd.merge(df_2, job_titles, how='inner', on='normalized_job_code')
    df_3 = df_3[['country_code', 'title', 'gender']]
    df_4 = pd.merge(df_3, country_names, how='inner', on='country_code')
    df_4 = df_4[['country', 'title', 'gender']]
    return df_4
