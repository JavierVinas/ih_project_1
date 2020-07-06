import pandas as pd
import sqlalchemy
import requests

# acquisition functions
# path = 'data/raw/raw_data_project_m1.db'

# Connect to personal_info database and return info into a dataframe

def acquire_personal_info(path):
    engine = sqlalchemy.create_engine(f'sqlite:///{path}')
    df_personal_info = pd.read_sql_query('SELECT * FROM personal_info', engine)
    return df_personal_info


# Connect to career_info database and return info into a dataframe

def acquire_career_info(path):
    engine = sqlalchemy.create_engine(f'sqlite:///{path}')
    df_career_info = pd.read_sql_query('SELECT * FROM career_info', engine)
    return df_career_info


# Connect to career_info database and return info into a dataframe

def acquire_country_info(path):
    engine = sqlalchemy.create_engine(f'sqlite:///{path}')
    df_country_info = pd.read_sql_query('SELECT * FROM country_info', engine)
    return df_country_info


# Access URL with country codes and corresponding country names and store it in a dataframe

def fetch_country():
    print("Accessing URL to extract country names")
    url = 'https://www.iban.com/country-codes'
    country_codes = pd.read_html(url, header=0)[0]
    country_codes = country_codes.drop(columns=['Alpha-3 code', 'Numeric'])
    country_codes.rename(columns={'Country': 'country', 'Alpha-2 code': 'country_code'}, inplace=True)
    return country_codes

# Access API job codes and store information in a dataframe

def fetch_job_titles(df_jobs_clean):
    print('Accessing API and extracting country names, please wait...')
    normalized_job_list = []
    job_codes = df_jobs_clean['normalized_job_code'].unique()[1:]
    for i in job_codes:
        r = requests.get("http://api.dataatwork.org/v1/jobs/{}".format(i))
        normalized_job_list.append(r.json())

    df_jobs = pd.DataFrame(normalized_job_list)
    df_jobs = df_jobs[['uuid', 'title']]
    df_jobs.columns = ['normalized_job_code', 'title']
    return df_jobs


