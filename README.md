# Streamlit in Dash

This repository provides a template for running a Streamlit app inside a Dash app. Follow the instructions below to set up and run the applications.

## Requirements

Ensure you have the following packages installed:

- streamlit==1.35.0
- dash==2.17.1

You can install the required packages using the provided requirements.txt file.

## Installation

1. Clone the repository

```sh
git clone https://github.com/derekmeegan/streamlit_in_dash.git
cd streamlit_in_dash
```

2. Create and activate a virtual environment (optional but recommended):

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```sh
pip install -r requirements.txt
```

## Usage

1. Run the Dash app. This will also start the Streamlit app in a separate thread:

```sh
python dash_app.py
```

2. Open your browser and navigate to http://127.0.0.1:8050 to see the Dash app with the embedded Streamlit app.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
