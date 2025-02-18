# Assignment 1: Python Refresher
  The purpose of this assignment is to get familiar with coding in Python using VSCode, committing changes to git, and refresh skills in installing libraries.
There are three total steps to this assignment. Step 0 (omitted): Create a GitHub repository. If you are reading this now, then this means this step was successfully completed.

## Necessary Packages
For this assignment, I utilized the functools, time, and matplotlib packages.

## Usage
To run echo.py and fib.py from assignment_1_python_refresher yourself, you'll want to first clone the repository, build/start the project locally in your preferred code editor, modify the source code to fit your needs, and run as necessary.

## Step 1: Python Programming Basics.
This step instructs the creation of a Python script echo.py that implements a method to take a user-defined string input
and return a string that resembles the input being echoed similar to if one were to shout on top of a mountain. To implement this, I created a function called echo() that takes
in two inputs: The string to echo and the number of times to echo which has a default value of 3 times. Then, my function truncates the input string such that only the last few characters remain.
The exact length is determined by the number of times the string is to be echoed or repeated. Then, my function prints this truncated string on a new line, then truncates the string again by one letter
and repeats this until the end of the string to which it prints one more line of a single period to signify the echo effect is finished. See the image below for an example when "Hello" is used as the input string to echo.
You can view my full source code [here](https://github.com/moore025/cs3980/blob/7f1802f80e93aa7d7bbe66bd3284ce1d71d62f70/assignment_1_python_refresher/echo.py).

![image](https://github.com/user-attachments/assets/f3eda3d1-7ac4-419c-987a-9fa87d8847c2)
<p align="center">
<em>Echo function output</em>
</p>

![image](https://github.com/user-attachments/assets/a780256a-1e8c-40b7-9952-de7abe36e1bb)
<p align="center">
<em>Full echo.py script</em>
</p>

## Step 2: Python Decorator Implementation
For this part of the assignment, I was instructed to make use of decorators and create a method called fib() that calculates the fibonacci sequence value of a given number. Along with this, I was instructed to use the lru_cache from the functools package to improve execution time as well as define a decorator named timer with a wrapper function that calculates the fibonacci sequence by calling fib and prints the result in a format that also includes the execution time. Along with this, I created a plot of execution time in seconds against the associated number used to calculate the fibonacci sequence of between 0 and 100 inclusive. With larger numbers requiring more calculations to be made to find the fibonacci sequence value, we expected runtime to increase as the input number increased. This was indeed observed in the plot shown below. One interesting thing to note about my plot is that my runtime was generally quicker than that of the example given to us. In fact, my maximum execution time (fib(100)) was around 0.00035 seconds. My full source code for this step can be found [here](https://github.com/moore025/cs3980/blob/27ec6d17a223e7db832677b2b00101389f88dea4/assignment_1_python_refresher/fib.py).

![image](https://github.com/moore025/cs3980/blob/8d26ab9d4665e31912bb1b4d3088a10a94a13886/assignment_1_python_refresher/fib_time_vs_num.png)
<p align="center">
<em>Execution time plot</em>
</p>

![image](https://github.com/user-attachments/assets/a31bddb0-97bd-4f32-8d78-81c345bd5781)
<p align="center">
<em>Example output in terminal from running fib.py</em>
</p>

![image](https://github.com/user-attachments/assets/81628db0-bd1b-4cdd-b439-d600a3ef3541)
![image](https://github.com/user-attachments/assets/f2d8dace-056f-4b35-8c01-ad9a9d196d67)
<p align="center">
<em>Full fib.py script</em>
</p>
