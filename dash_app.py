import streamlit as st
import threading
import subprocess
from dash import Dash, html

def run_streamlit_app(file_name):
    subprocess.run(['streamlit', 'run', file_name, '--server.port=8501'])

app = Dash()

app.layout = [
    html.Div('This is the dash app.'),
    html.Iframe(
        src = 'http://localhost:8501',
        style = {
            'width': '100%',
            'height': '400px',
            'border': 'none'
        }
    )
]

if __name__ == '__main__':

    threading.Thread(target = run_streamlit_app, daemon=True, kwargs = dict(file_name = 'streamlit_app.py')).start()
    app.run(debug = True)