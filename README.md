# Insights-DataCodingChallenge
Problem Statement

The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land. Handling and analyzing such large data-sets is tedious hence I tried simplifying the data by generating a summary of this on a per-Month, per-Border, per-Type (Pedestrians, Vehicles etc) basis. Summary includes total crossing for that border, type and running-average each month.  


Approach: Below are the major parts of the code and this also provides a sneek-peak of my thought process

1. Input / Output 
   As per-the problem statement, the code uses a CSV file as an input and the output is in CSV format as well.
   The path the input / output file needs to specified by the user. 

2. Choosing the data-structure 
   Since this data-set had relational links between different fields example: border-to-measure i.e. US-Mexico : Pedestrians etc. 
   I found Dictionary to be the most applicable data-structure for this problem. 
   Here is an over-view of the dict data-structure used here:
   border_crossing --> [ DATE ] --> [ BORDER-NAME] --> [ MEASURE] --> [ SUM / Running-Average ] 
   Choosing this data-structure greatly simplified the further steps.  

3. Corner-cases 
   I tried to handle the corner-cases based on the data-set provided and also preempted few cases. Here are few examples:
   a. How to handle the running-average for the very 1st month for a measure 
   b. How to handle the sum / running-average for a measure if not specified in a given month 

4. Scalability 
   One of the key focus areas for this solution was scalability, I tried to make this code scalable for these parameters. 
   a. If a new Border-Crossing data-set is used the code can handle:
     i.  New Border / new countries. 
     ii. New measure type example: the border crossing by air etc. 
       
5. Testing
   This code was tested on the data-sets provided as well as some local testing data-sets. 
   Also, this code was tested on my personal python setup and the website http://ec2-3-225-56-40.compute-1.amazonaws.com/test-my-repo-link
   This helped flush out any issues with environment etc. 
   
   


