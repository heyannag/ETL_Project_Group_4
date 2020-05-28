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
