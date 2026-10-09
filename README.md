# Cyberbullying Detection System Documentation

## Introduction
This repository contains the software specification and implementation assets for a cyberbullying detection system with front-end integration. The project combines machine learning, a web interface, and a Node.js server to classify input text and present the result to the user.

### Project Goals
- Detect cyberbullying-related language in text input.
- Provide a simple front-end for users to submit text and view predictions.
- Support awareness and response to harmful online behavior through automated detection.

### What the System Does
- Accepts user-entered text from the web interface.
- Sends the text to the backend server for processing.
- Uses a Python-based machine learning model to analyze the text.
- Returns a prediction such as a cyberbullying category or a non-cyberbullying result.

## Installation
### Prerequisites
- Internet connection
- Laptop or desktop computer
- IDE (Integrated Development Environment)
- Python 3.x
- Node.js

### Installation Steps
1. Clone the repository or download the project as a ZIP file.
2. Update any file paths used in `Cyberbullying_Detection_System.py` and `node.js` if required.
3. Install the Python dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
4. Install the Node.js dependencies if they are not already installed.
5. Start the backend server with:
   ```bash
   node node.js
   ```

## Usage
1. Open the user interface in your browser.
2. Enter text into the input field.
3. Click the submit button.
4. Review the prediction returned by the system.

## Features
- Cyberbullying detection for text input.
- Front-end integration for user interaction.
- Machine learning-based classification.
- Backend communication between the web interface and the Python model.

## Dependencies
- Python 3.x
- scikit-learn
- pandas
- NumPy
- NLTK
- TensorFlow
- Node.js
- Express.js
- PythonShell (Node.js module)
- Body-parser (Node.js module)

## Project Structure
### Main Files and Directories
- `node.js`: Server-side code that handles requests and coordinates communication with the Python script.
- `User_Interface.html`: Front-end interface for submitting text and displaying predictions.
- `Cyberbullying_Detection_System.py`: Python script that implements the detection workflow.
- `Dataset`: Training data used for model development.

### Key Components
- **Node.js Server**: Receives requests and passes data between the user interface and Python model.
- **User Interface (HTML)**: Provides a simple interface for submitting text and viewing results.
- **Python Script**: Performs preprocessing and prediction using the trained model.
- **Dataset**: Contains labeled text samples used to train the classification model.

## Troubleshooting
- If you receive a port-related error, another process may already be using the server port. Use `lsof -i :3001` to identify the process.
- Because of limited dataset diversity, some clearly abusive sentences may be misclassified. Improving the training data may help.
- For additional troubleshooting guidance, refer to the video included in the project folder.

## Credits
- Isaiah Mocombe
- Jordan Mozebo
- Daniel Searcy
- Jalen Shine
- Genea Taylor

## Contact Information
For more information, please use the email in the GitHub profile or contact each contributor.

## Last Section
This repository is maintained as part of COMP710-001 Software Specifications and Design.
