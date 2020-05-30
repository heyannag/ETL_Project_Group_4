# ETL Project | Group 4

## Team
* Kara
* Bean
* Anna


## Table of Contents
* [Objective](#Objective)
* [Technologies](#Technologies)
* [ETL](#ETL)
* [ToDo](#ToDo)
* [Troubleshooting](#Troubleshooting)

# Objective | Create a Database Utilizing ETL on Real Datasets
Organize data from multiple databases in order to determine similar characteristics of Grammy-winning songs between the years of 2010 and 2019 per streaming platform Spotify.

    * Extract: your original data sources and how the data was formatted (CSV, JSON, pgAdmin 4, etc).
    * Transform: what data cleaning or transformation was required.
    * Load: the final database, tables/collections, and why this was chosen.

## Project Proposal (add/export Google Doc in repo)

# Technologies
* Pandas
* Python3
* PostgreSQL

# ETL
## Process Documentation

Our datasets were obtained on Kaggle at the following links:

* [Top Spotify Songs 2010-2019](https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year)

* [Grammy Awards](https://www.kaggle.com/unanimad/grammy-awards)

## E | Extract
* Read in CSV data in a Jupyter notebook file with Pandas
            '''
            grammy_df=pd.read_csv('the_grammy_awards.csv')
            grammy_df.head()
            '''


## Data Cleanup & Analysis

Once you have identified your datasets, perform ETL on the data. Make sure to plan and document the following:

* The sources of data that you will extract from.

* The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).

* The type of final production database to load the data into (relational or non-relational).

* The final tables or collections that will be used in the production database.

You will be required to submit a final technical report with the above information and steps required to reproduce your ETL process.

## Project Report

At the end of the week, your team will submit a Final Report that describes the following:

* **E**xtract: your original data sources and how the data was formatted (CSV, JSON, pgAdmin 4, etc).

* **T**ransform: what data cleaning or transformation was required.

* **L**oad: the final database, tables/collections, and why this was chosen.

Please upload the report to Github and submit a link to Bootcampspot.

- - -

### Copyright

Coding Boot Camp © 2019. All Rights Reserved.
