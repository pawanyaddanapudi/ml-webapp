# Flask Web Application - Linear Regression
For the following attributes of a basketball player, this web application builds linear regression model on loading home page.
In the home page, you can then provide new player attributes to predict his average points.

Independent attributes:
1. height_ft = Height in feet
2. weight_pd = Weight in pounds
3. successfieldgoals% = percent of successful field goals (out of 100 attempted) (0.xx format)
4. successfreethrows% = percent of successful free throws (out of 100 attempted) (0.xx format)

Dependent variable:
1. avg_points = average points scored per game

```ml-webapp-main.py``` is coded in Python 3.7

Install Python 3.7 (https://www.python.org/downloads/) and following packages(using pip) before running the script

Packages:
1. pandas
2. sklearn
3. flask

To run the application:

```python3 ml-webapp-main.py```

- Make sure the data files are the same location as py file

Web application runs on port 9000 as in the code. You can configure to run on different port.

Open the browser and load "http://localhost:9000/"

Fill in the inputs and click on "Predict"

The output page will have inputs as well as predicted average score of basket ball player.

Note: The data has been downloaded from https://college.cengage.com/mathematics/brase/understandable_statistics/7e/students/datasets/mlr/frames/frame.html
