# Election_Analysis

## Overview of Election Audit
A Colarado Board of Elections employee has been given the following tasks to complete the election audit of a recent local congressional election. The inital data used is the combination of mail-in ballots (hand counted), punch cards(machine counted) and direct recording electronic machines (computer counted).


1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each cndidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote
6. Get a complete list of counties that received votes
7. Calculate the voter turnout for each county
8. Calculate the percentage of votes from each county out of the total count
9. Determine the county with the highest turnout

## Election-Audit Results
* There were **369,711** votes cast in the election.
* Number of votes and corresponding percentage of total votes per county were:
    * Jefferson: 10.5% (38,855)
    * Denver: 82.8% (306,055)
    * Arapahoe: 6.7% (24,801)
* County with the largest number of votes is:
    * Denver
* The candidates and coresponding votes were:
    * Charles Casper Stockham: 23.0% (85,213)
    * Diana DeGette: 73.8% (272,892)
    * Raymon Anthony Doane: 3.1% (11,606)
* The winner of the election was:
    * Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary
We determined the winning candidate and county with highest number of votes in this project.

We can use the same code for determining the winner from the elections results of other congressional districts, senatorial and local elections. We would need election data corresponding to those.


### Ways the code can be used with some modifications:
(1) Similar to winning candidate votes, we can modify the code to find the candidate with the least number of votes. That can be achieved by

a) *instead of this*

winning_candidate = ""

winning_count = 0

winning_percentage = 0

*do*

least_candidate = ""

least_count = 1000000

least_percentage = 100

b) *changing the logic from this*:

if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

*to*:

if (votes < least_count) and (vote_percentage < least_percentage):

            least_count = votes
            least_candidate = candidate_name
            least_percentage = vote_percentage

(2)
