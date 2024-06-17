# BMI Calculator

Welcome to the BMI Calculator project! This project is a simple web application that calculates your Body Mass Index (BMI) based on your weight and height. The application is built using Streamlit, a popular Python library for creating interactive web applications.

## Features

- Input fields for name, gender, age, address, hobbies, weight, and height.
- Calculation of BMI based on the entered weight and height.
- Display of BMI value and health status.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3.8 (or later) installed on your machine.
- You have `pip` (Python package installer) installed.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/bmi-calculator.git
    cd bmi-calculator
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment**:

    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, use the following command:
```bash
streamlit run main.py
