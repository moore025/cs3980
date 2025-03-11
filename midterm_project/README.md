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

If you change your mind about a review, you can edit it and update it as necessary by clicking the "edit" button of the respective review. Additionally, you can also delete a review by clicking the "delete" or "trash" icon on the respective review.
