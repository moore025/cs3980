# Midterm Project
I made an Iowa City restaurant reviewer web app called HawkBites that allows for users to share their own personal reviews on local restaurants. Each review requires the restaurant name, a rating out of 10, and a review description. This app was an expansion upon our in-class demo Todo App, and I added functionality to share and update ratings as well as redesigning the interface.

## Necessary Packages and Languages
For this project, I mainly used the Uvicorn and FastAPI packages in order to implement CRUD (Create, Read, Update, and Delete) operations for users of the webpage to be able to submit, update, and delete reviews. For languages, I coded the backend in Python, and for the backend I utilized HTML and css to design the interface as well Javascript to handle changes to the webpage contents.

## Usage
In order to use my application, you will first need to clone my repository, ensuring you have all necessary files. Then, you will want to open the project in your preferred code editor, and download all necessary packages. Next, navigate to the correct path in console and enter the following command in order to host the application. 
```console
uvicorn main:app --reload
```
Once open, you can locally add, edit, and delete Iowa City restaurant reviews. Upon opening the webpage in your browser, you will be met with this screen: ![image](https://github.com/user-attachments/assets/ba7190ae-26c1-4ad3-93aa-e80995e7e8ee)

From here, you can add a review by clicking the "Add New Review" button which will open a form for you to fill out the contents of your review including the restaurant name, your rating 1-10, and you review description. Once you fill out all fields, you can click "Add" to submit your review, and it will be posted in the reviews section on the main page.
![image](https://github.com/user-attachments/assets/55cae84b-5833-4754-af5e-ca886d2888d0)


![image](https://github.com/user-attachments/assets/e2883b97-0499-4807-914d-823f1871648a)

If you change your mind about a review, you can edit it and update it as necessary by clicking the "edit" button of the respective review. 
![image](https://github.com/user-attachments/assets/3f3235f3-7e91-49c1-82fe-70a53bf155b6)
![image](https://github.com/user-attachments/assets/9f3e0119-23d9-4a50-ad73-6350cef2956d)


Additionally, you can also delete a review by clicking the "delete" or "trash" icon on the respective review. Make sure that you do not need the review anymore, though, because once the trash icon is clicked the review will be deleted without any extra confirmation.

## Creation
Once again, this project was heavily influenced by our in-class demos and was an expansion upon the Todo App. Most of the changes that I made to the Todo App code were stylistic in order to fit the theme of an IC restaurant review application including changing the appearance in the [style.css](https://github.com/moore025/cs3980/blob/ed9c9a8d57fa327d731d0ed9fd7b57e96bf2eaac/midterm_project/frontend/style.css) file, changing form labels and review output format in the [index.html](https://github.com/moore025/cs3980/blob/ed9c9a8d57fa327d731d0ed9fd7b57e96bf2eaac/midterm_project/frontend/index.html) file, and adding rating functionality to the [model.py](https://github.com/moore025/cs3980/blob/ed9c9a8d57fa327d731d0ed9fd7b57e96bf2eaac/midterm_project/model.py) class as well as updating CRUD operations in [review.py](https://github.com/moore025/cs3980/blob/ed9c9a8d57fa327d731d0ed9fd7b57e96bf2eaac/midterm_project/review.py) and [main.js](https://github.com/moore025/cs3980/blob/ed9c9a8d57fa327d731d0ed9fd7b57e96bf2eaac/midterm_project/frontend/main.js) to handle this additional variable.

## Next Steps
If I were to advance this project for our final project, the first changes that I would make would be to first implement searching functionality that allows for users to search up Iowa City restaurants to see what locals think about them. This would involve implementing a new restaurant class that might have key values like average rating, address, website, menu, etc. that would be displayed upon to the user upon searching a restaurant. I think that there are many ways to move forward with this idea and many changes that could be made to transform the user experience, which makes me excited about the potential of this idea.
