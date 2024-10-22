
# Chocolate House App

Welcome to the Chocolate House App! This application allows you to manage flavors, ingredients, and customer suggestions in a delightful chocolate shop environment.


## Features
- Add, view, and delete flavors
- Add, view, and delete ingredients
- Submit and view customer suggestions
- User-friendly interface via Streamlit

## Technologies Used
- Python
- SQLite
- Streamlit

## Requirements
To run this application, you need:
- Python 3.x
- Pip (Python package installer)

### Python Libraries
- streamlit
- sqlite3 (included with Python)

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/Wuxxian/chocolate-house.git
   cd chocolate-house
   ```

2. Install the required packages:

   You can create a virtual environment and install the requirements using the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Running the Application Locally
1. To run the command-line application, execute:

   ```bash
   python main.py
   ```

2. To run the Streamlit application, execute:

   ```bash
   streamlit run app.py
   ```

### Running the Application with Docker
1. Build the Docker image:

   Navigate to the directory containing your Dockerfile and run:

   ```bash
   docker build -t chocolate-house-app .
   ```

2. Run the Docker container:

   To run the container, use the following command:

   ```bash
   docker run -p 8501:8501 chocolate-house-app
   ```

   Access the Streamlit app in your web browser at `http://localhost:8501`.

