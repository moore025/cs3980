# Assignment 2: API JSON HTML JavaScript
For this assignment, I was tasked with reading and displaying data about yearly US population into a table on an HTML webpage. The data was retrieved from an [api endpoint](https://datausa.io/api/data?drilldowns=Nation&measures=Population).

## Necessary Packages
For this assignment, I used resources from fastAPI.

## Usage
To access my tabulated population data HTML webpage, you will first want to clone my repository, and open [index.html](frontend/index.html).
## Step 1: Create a web page to display US Population data.
To create my webpage, I mainly utilized two files in my frontend directory: an [HTML file](frontend/index.html) to create the webpage and a [JavaScript file](frontend/main.js) to interact with the population data from the api endpoint by parsing through it and displaying it in the table in my HTML file. A lot of this code was based on our in-class lecture demos.

In creating my HTML file, I first set the title to "US Population Data" and included an image of the US flag. Then, I created a table and made its header row contain "Year" and "US Population". Then, I defined a unique identifier for subsequent rows for [main.js](frontend/main.js) to manipulate as it reads in data from the api endpoint.

For my JavaScript file, I defined two main functions that were used to get population data as well as display population data. My get function accessed and retrieved the data from the api endpoint, logged the data in console, and then called my display population data function. My display population function mapped the year and corresponding population into a given row and returned it to the HTML file for display.

Attached below is a screenshot of my webpage.
![image](https://github.com/user-attachments/assets/eca4dd50-26c3-497a-9f51-2b782d59628c)
