import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
#from p_reporting import m_reporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Set chart type')
    parser.add_argument("-p", "--path", help="Introduce the path...", required=True, dest='Path1')
    parser.add_argument("-c", "--country", type=str, dest="country", help="Type in a country name to analyze...", default="")
    args = parser.parse_args()
    return args

def main(arg1,arg2):
    data_personal_info = mac.acquire_personal_info(arg1)
    print('A dataframe with personal info was created')
    clean_gender = mwr.wrangle(data_personal_info)
    country_names = mac.fetch_country()
    print('A dataframe with country info was created')
    career_info = mac.acquire_career_info(arg1)
    print('A dataframe with career info was created')
    job_titles = mac.fetch_job_titles(career_info)
    print('Job titles successfully retrieved')
    country_info = mac.acquire_country_info(arg1)
    main_df = mwr.merge_dfs(country_info,career_info,clean_gender,job_titles,country_names)
    print('Main dataframe retreived')
    final_table = man.analyze(main_df)
    print('Final table with the results has been created in /data/results folder')
    table_country = man.filter_country(arg2, final_table)
    table_country.to_csv(r'data/results/final_table.csv', index=False, header=True)



if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments.Path1, arguments.country)