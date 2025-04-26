# Assignment 4: User Login
For this assignment, I was tasked to implement user login features to my midterm project: HawkBites - an Iowa City restaurant reviewer app.

## Necessary Packages and Languages
For this project, I mainly used the Uvicorn and FastAPI packages in order to implement CRUD (Create, Read, Update, and Delete) operations for users of the webpage to be able to submit, update, and delete reviews. For languages, I coded the backend in Python, and for the backend I utilized HTML and css to design the interface as well Javascript to handle changes to the webpage contents.

## Usage
To see complete usage directions for my application, please reference my midterm_project directory. For this assignment, you will just need to click the "Log In" button. From this screen, you can log into an existing account. I am still working on implementing a sign up feature, so in the meantime you can only sign into accounts that have already been created. Therefore, if you would like to log in, please use my already generated test account ``` username: Test ``` ```password: Test ```.

## Creation
For this project, I heavily referenced our in-class demo for Todo-App-2. Therefore, I had many of the CRUD operations already created, but I just had to make adjustments to my personal midterm app's frontend so that it handled these CRUD operations correctly for the context of the review app. Upon reaching the main landing page of my app, you will see a new "Log In" button in blue.
![image](https://github.com/user-attachments/assets/9a15078b-78a1-410f-8f39-f2d367c2ffa1)
Upon clicking this button, the login form will be opened.
![image](https://github.com/user-attachments/assets/8e85baa3-116a-466e-9d28-93ae4c3ab2e2)
If you enter in a blank username and password, you will be notified.
![image](https://github.com/user-attachments/assets/835bfe0f-7788-4ccd-9d94-5248bc8950ea)
If you enter in a correct username and password (for example, just "Test" and "Test") you will receive a 200 OK code. If you get the incorrect username and password combination, you will receive a 401 UNAUTHORIZED code.

## Next Steps
The next steps for this project would be to improve sign-up functionality. I have already made a sign up button on the frontend, but I am still trying to configure it with the backend.
