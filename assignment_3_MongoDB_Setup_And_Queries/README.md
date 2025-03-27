# Assignment 3: MongoDB Setup and Queries
This assignment was a simple exercise to explore MongoDB by creating an account, creating a cluster, adding a user (myself), loading sample data, and generating a connection string to allow for access through MongoDB Compass Community Edition. Once all of the adminastrative steps were complete, to complete this assignment I had to generate two queries and capture a screenshot of each query and associated results that will be described below.

# Step 4: Assignment
## Query 1
For this query, I was to find all movies with a runtime greater than 200 minutes aired in the year 1983. The results were to only include runtime, title, and year as well as be ordered by runtime in ascending order. In order to make this query, I had to consider both the search conditions as well as output fields. I wanted to make sure that my find query only found movies with a runtime GREATER than 200 minutes, so that meant I had to utilize the comparison operator of $gt. Next, since I only wanted to return the fields of runtime, title, and year I had to specify each field to true/1 and since _id is returned by default, I had to explicitly set it to false/0. The last thing I had to consider in making my query was to output the results in ascending order by runtime. For this, I utilized the .sort method and chose runtime to be set to 1/ascending (in contrast to -1/descending). That said, here was my query 
`db.movies.find({runtime:{$gt:200}, year:{$eq:1983}}, {_id:0,runtime:1,title:1,year:1}).sort({runtime:1})`
and my resulting screenshot is below.
![image](https://github.com/user-attachments/assets/79c71ed5-93b0-486d-a302-d8f7e4998921)


## Query 2
For this query, I was to find all movies aired after the year 2014 and with an imdb rating greater than 9 then output the results to only display the imdb rating, title, and year. I used the same idea as my previous query in order to handle the condition of finding movies with a year GREATER than 2014, but in order to handle the imdb rating condition, I had to be careful in how I referenced the rating because rating was a subfield of the imdb field. To handle this, I simply called "imdb.rating". I didn't have to take any additional result formatting into account, so my final query was simply
'db.movies.find({"imdb.rating":{$gt:9}, year:{$gt:2014}}, {title:1,year:1,"imdb.rating":1})`
and my resulting screenshot is below.
![image](https://github.com/user-attachments/assets/caafd4bd-aed0-4a9b-b9b2-68ecbda3fb81)

