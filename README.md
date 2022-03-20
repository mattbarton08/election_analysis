# Election Analysis

## Overview of Election Audit
The purpose of this analysis was to look over all of the voting data from the election and determine the total vote count, county voting data, and winning candidate.

## Election-Audit Results

### How many votes were cast in this congressional election?
I used code to count up all of the votes from the data. All in all, there were 369,711 votes cast.
![vote_count_code](https://i.imgur.com/EWGa87V.png)
        
### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
After adding variables for county names and number of votes, I used similar code as before to count the votes that each county cast. Here were the results:<br>
Jefferson: 10.5% (38,855)<br>
Denver: 82.8% (306,055)<br>
Arapahoe: 6.7% (24,801)<br>
<br>Here is the code I used to retrieve the data and write it to a text file:
![county_vote_code](https://i.imgur.com/A7NGqcT.png)

### Which county had the largest number of votes?
The county with the largest number of votes was Denver County, which had 306,055 votes and  82.8% of the total vote.

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Charles Casper Stockham: 23.0% (85,213)<br>
Diana DeGette: 73.8% (272,892)<br>
Raymon Anthony Doane: 3.1% (11,606)<br>

Here is part of the code I used to retrieve this data:
![candidate_vote_code](https://i.imgur.com/w7z6DOY.png)

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
The winner of the election was Diana DeGette. She received 272,892 votes which was 73.8% of the total votes.

## Election-Audit Summary: 
This python script that I created for this election audit could be used for any election that you would need to look over. I wrote it in such a way that the variables can be applied to any data that is formatted in the same way. If there were more candidates or counties added, for example, the code would still run in exactly the same way and return accurate results.

The code can also be modified to work better for other elections you may need to audit. For example, if you needed to have ordinaces that were voted on added, I could add a dictionary with the ordiances and add a simple boolean operator to determine whether the ordinace passed or failed. And if you wanted to add multiple elected positions, the scripte could include dictionaries for more than one position and return a similar output to the one produced here.
