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
* Downloaded both CSV datasets 
* Read in CSV data in a Jupyter notebook file with Pandas
       
       '''
        grammy_df=pd.read_csv('the_grammy_awards.csv')
        grammy_df.head()
       '''
## T | Transform

  Grammy Dataset
   Limited dataset to only include Awards that were given to *songs*
      
      '''
       song_df=grammy_df[grammy_df['category'].str.contains('Song')]
       '''
      
   Reduced dataset to years 2010 - 2019 to more acurately compare with the obtained Spotify dataset
      
      '''
      grammy_df = grammy_df.loc[grammy_df["year"]> 2009]
      grammy_df.head()
      '''
      
  Spotify Dataset proved to have high quality data, however, when importing the CSV into PgAdmin4 we ran into an unknown/foreign character UTF8 error and the file could not import. We resolved this error by noting the encoding type to LATIN1. 
  
  In this stage we uncovered the relational structure of our datasets is the Song/Track's Name. This information was located in Grammy's nominee column and Spotify's title column. 
  
## L | Load

We decided to work in PostgreSQL due to the relational structure of our datasets. 

### Steps: Tables/Collections

Grammy 
	Created table with the following columns: 
   
     '''
      DROP TABLE IF EXISTS grammy;
         CREATE TABLE grammy(
           year INT NOT NULL,
           category VARCHAR NOT NULL,
           title VARCHAR NOT NULL,
           workers VARCHAR NOT NULL,
           winner VARCHAR NOT NULL
           );
      '''

Spotify 
Created table with the following columns: 

    '''
     DROP TABLE IF EXISTS spotify;
           CREATE TABLE spotify(
               id VARCHAR (30) NOT NULL,
               title VARCHAR NOT NULL,
               artist VARCHAR(30) NOT NULL,
               top_genre VARCHAR(30) NOT NULL,
               year INT NOT NULL,
               bpm INT NOT NULL,
               nrgy INT NOT NULL,
               dnce INT NOT NULL,
               dB INT NOT NULL,
               live INT NOT NULL,
               val INT NOT NULL,
               dur INT NOT NULL,
               acous INT NOT NULL,
               spch INT NOT NULL,
               pop INT NOT NULL
               );
         '''

We used the JOIN function to combine our two tables into the database. More specifically, we used an INNER JOIN to combine the information under *nominee* (Grammy) and *title* (Spotify).

      '''
      SELECT spotify.id,
           spotify.title,
           spotify.artist,
           spotify.top_genre,
           spotify.year,
           spotify.bpm,
           spotify.nrgy,
           spotify.dnce,
           spotify.db,
           spotify.live,
           spotify.val,
           spotify.dur,
           spotify.acous,
           spotify.spch,
           spotify.pop,
           grammys.category,
           grammys.nominee,
           grammys.workers,
           grammys.winner
         FROM spotify
         INNER JOIN grammys ON
         spotify.title = grammys.nominee;
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
