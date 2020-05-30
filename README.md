# ETL Project | Group 4

## Create to create Top 5 Playlists in a user's Spotify Account 

## Table of Contents
* [Technologies](#Technologies)
* [Setup](#LocalSetup)
* [ToDo](#ToDo)
* [Troubleshooting](#Troubleshooting)


## Technologies
* [Youtube Data API v3]
* [Spotify Web API]
* [Requests Library v 2.22.0]
* [Youtube_dl v 2020.01.24]

## LocalSetup
1) Install All Dependencies   
`pip3 install -r requirements.txt`

2) Collect You Spotify User ID and Oauth Token From Spotfiy and add it to secrets.py file
    * To Collect your User ID, Log into Spotify then go here: [Account Overview] and its your **Username**
    ![alt text](images/userid.png)
    * To Collect your Oauth Token, Visit this url here: [Get Oauth] and click the **Get Token** button
    ![alt text](images/spotify_token.png)

3) Enable Oauth For Youtube and download the client_secrets.json   
    * Ok this part is tricky but its worth it! Just follow the guide here [Set Up Youtube Oauth] ! 
    If you are having issues check this out [Oauth Setup 2] and this one too [Oauth Setup 3] 

4) Run the File  
`python3 create_playlist.py`   
    * you'll immediately see `Please visit this URL to authorize this application: <some long url>`
    * click on it and log into your Google Account to collect the `authorization code`


## ToDo
* Tests
* Add Error Handling

## Troubleshooting
* Spotify Oauth token expires very quickly, If you come across a `KeyError` this could
be caused by an expired token. So just refer back to step 3 in local setup, and generate a new
token!  


   [Youtube Data API v3]: <https://developers.google.com/youtube/v3>
   [Spotify Web API]: <https://developer.spotify.com/documentation/web-api/>
   [Requests Library v 2.22.0]: <https://requests.readthedocs.io/en/master/>
   [Account Overview]: <https://www.spotify.com/us/account/overview/>
   [Get Oauth]: <https://developer.spotify.com/console/post-playlists/>
   [Set Up Youtube Oauth]: <https://developers.google.com/youtube/v3/getting-started/>
   [Oauth Setup 2]:<https://stackoverflow.com/questions/11485271/google-oauth-2-authorization-error-redirect-uri-mismatch/>
   [Youtube Video]:<https://www.youtube.com/watch?v=7J_qcttfnJA/>
   [Youtube_dl v 2020.01.24]:<https://github.com/ytdl-org/youtube-dl/>
   [Oauth Setup 3]:<https://github.com/googleapis/google-api-python-client/blob/master/docs/client-secrets.md/>
=======
# ETL_Project_Group_4
Where is the data coming from? (at least two sources)
Apple Music API music playlists 
Spotify API music playlists  
Grammy’s (https://www.kaggle.com/unanimad/grammy-awards)

Where is the data going to? 
postgres

What will be the structure of the data in the final database? What tables/columns/types/etc.

End goal to display multiple top 5’ playlists denoted by characteristic, 

Song title 		String
Artist name 		String
User streams 	INT
Release Date 	FLOAT
Added Date 		FLOAT
Song of the Year 	String
Grammy winner?	Boolean
Number of playlists	INT


Random Thoughts:

Add tracks to a new playlist on the user’s Spotify account

Are there genres or characteristics that shine on one platform over the other.
2006 – spotify
2003 – iTunes/Apple Music - 2015

***Final product creates new Spotify playlist 
 
How do we account for purity of data? – limit to specific playlist

Anna
View authorization steps for Spotify API authorization
Discovered OAuth examples Github repository and reviewed before installing Node.js
Installed node.js

Kara
Downloaded Past Grammy Winners CSV from Kaggle
Imported to Pandas and saved only the Grammy categories for individual songs into a data frame.
Exported to a new CSV and pushed to a git branch

Lisa
View authorization steps for Apple Music API
Create apple certificate
Create private key
Manage identifiers
Troubleshoot 
Created branch for git work
Started py doc for import.
>>>>>>> 336ff09ae81777e3241b721f63018ee07de97bc2
