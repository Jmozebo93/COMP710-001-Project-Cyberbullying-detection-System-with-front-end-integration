# Cyberbullying Detection System Documentation

## Introduction
- Brief overview of the project
•	According to Pew Research Center, close to half of teens in the United States have been victims of online harassment [1].
•	Over 40% of adult internet users report having personally experienced cyberbullying in their lifetime [2].
- Purpose and objectives of the cyberbullying detection system
•	Implementing a user-friendly front-end interface for real-time cyberbullying detection.
•	Support mental well-being by providing a reliable tool for identifying and addressing cyberbullying.

## Installation
- Prerequisites
•	Internet, Laptop, IDE (Integrated Development Environment)
- Installation steps
•	Cloning the repository or download the zip file or the project.
•	Make sure to change the file path inside python file (Cyberbullying_Detection_System.py) and the server (node.js).
•	Before installing the dependencies go to the directory where the file ‘requirements.txt’ is and enter the following command ‘pip install -r requirements.txt’, this command will install all the dependencies.
  - Running the system
•	In the directory where the server file is, enter the following command ‘node node.js’ to start the server. 

## Usage
•	After the sever has started access the user interface
•	Enter input, click on the submit button, and obtain the result.

## Features
•	Cyberbullying Detection: The system can detect instances of cyberbullying in text data, classifying them into categories such as "racism," "sexism," or "none."
•	Supervised Machine Learning: Utilizes supervised machine learning techniques to learn from labeled data and make predictions based on input features.

## Dependencies
•	Python 3.x
•	scikit-learn
•	pandas
•	NumPy
•	NLTK
•	TensorFlow
•	Node.js
•	Express.js
•	PythonShell (Node.js module)
•	Body-parser (Node.js module)

## Project Structure
Overview
•	The cyberbullying detection system project is organized into several directories and files, each serving a specific purpose in the system's functionality.
Main Files and Directories
•	node.js: This file contains the server-side code written in Node.js. It handles incoming requests from the user interface, processes them, and communicates with the Python script for cyberbullying detection.
•	User_Interface.html: This HTML file represents the user interface of the system. It allows users to input text data for cyberbullying analysis and displays the results.
•	Cyberbullying_Detection_System.py: This Python script implements the cyberbullying detection algorithm. It preprocesses the input text, applies a machine learning model to predict cyberbullying, and returns the result to the server.
•	Dataset: This directory contains the dataset used for training the cyberbullying detection model. It typically includes CSV files containing text data and corresponding labels.
Key Components/Modules
•	Node.js Server: Responsible for handling HTTP requests and responses, as well as orchestrating communication between the user interface and the Python script.
•	User Interface (HTML): Provides an interactive interface for users to input text data and view the results of cyberbullying analysis.
•	Python Script: Implements the cyberbullying detection algorithm using a machine learning model. It preprocesses the input text, applies feature extraction, and predicts the presence of cyberbullying.
•	Dataset: Contains the training data used to build the cyberbullying detection model. It includes text samples labeled with their corresponding cyberbullying annotations, which are used to train and evaluate the model.

## Troubleshooting
- Common issues and their solutions
•	If you get a ‘throw ‘ error message it means that another process is running on the port used by the server. Enter the following command ‘lsof -i :3001’ to check which process is using port 3001. To solve this problem, change the port number to a different one.
•	Due to the lack of diversity in our dataset, the model might misclassify some sentences that are clearly cyberbullying as not containing element of cyberbullying. It is advised to used labels like ‘bitch’, terrorist’; for example, the following sentence “I’m not sexist, but women should not” will be labeled as cyberbullying. 
- Troubleshooting tips
•	For any further troubleshooting tips, refer to the video in the project folder.


## Credits
•	Isaiah Mocombe
•	Jordan Mozebo
•	Daniel Searcy
•	Jalen Shine
•	Genea Taylor

## Contact Information
•	For more information, please use the email in the GitHub profile or contact each contributor. 
