# Ironhack Data Analytics Project 

This README file explains the process taken in the pipeline project required in the Data Analytics Bootcamp inside Ironhack.

![Image](https://www.finsmes.com/wp-content/uploads/2019/07/ironhack.jpg)

---

## **Challenge 1**
The aim of this project is to analyzed how gender is represented in data jobs. Therefore, we will analyze the percentage of male and female by country and job given our dataset.


## **How to execute the script**
Before initializing the main_script.py you have to **install the libraries located in the requirements.txt**
In order to execute the main_script.py you have to give two arguments to the main function:
- Path: the path where is located your database
- Country: the country name within the European Union

Example: >>> python main_script.py -p data/raw/raw_data_project_m1.db -c Spain


## **Project Structure**
The pipeline is divided into 3 modules:
- Acquisition
- Wrangling
- Analysis

Each module performs some functions that are called from the main_script.py

## **Inputs or requirements** 
- Raw data containing the database (there are 4 dataframes)
- API with the job codes and job titles --> it is used to map those job codes and retrieved the corresponding job title
- URL with the country names --> it is used to extract the full country names of all European countries

### :file_folder: **Folder structure**
```
└── ih_project_1
    ├── __trash__
    ├── .gitignore
    ├── .env.txt
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── notebook1.ipynb
    │   └── notebook2.ipynb
    ├── p_acquisition
    │   ├── m_acquisition.py
    ├── p_analysis
    │   ├── m_analysis.py
    ├── p_reporting
    │   ├── m_reporting.py
    ├── p_wrangling
    │   ├── m_wrangling.py
    └── data
        ├── raw
        ├── processed
        └── results
```


