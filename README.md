Here’s a clear and professional README draft for your project:

---

# Obesity Level Classification Project

## Overview

This project focuses on predicting an individual's obesity level based on various lifestyle, demographic, and health-related features. The workflow begins with exploratory data analysis and model experimentation in Jupyter Notebook (`.ipynb`), followed by model deployment using FastAPI and a user-friendly interface built with Streamlit.

## Workflow

1. **Model Development**

   * Conducted data preprocessing and exploratory analysis using the provided obesity dataset.
   * Trained two machine learning models:

     * **Random Forest Classifier**
     * **AdaBoost Classifier**
   * Evaluated both models and selected the one with the best performance.
   * Saved the best-performing model into a `.pkl` file using Joblib.

2. **API Deployment**

   * Built a REST API using **FastAPI**.
   * The trained model was loaded from the `.pkl` file.
   * Implemented a `/predict` endpoint to return predictions based on user inputs.

3. **User Interface**

   * Developed a web-based interface using **Streamlit**.
   * The interface allows users to input their personal data (e.g., age, gender, height, weight, dietary habits, lifestyle factors).
   * The application communicates with the FastAPI backend and displays the predicted obesity level.

## Project Structure

```
.
├── ObesityDataSet2.csv        # Dataset
├── notebook.ipynb             # Jupyter Notebook for training and evaluation
├── pickle.pkl                 # Trained model (best performing)
├── fastapii.py                # FastAPI backend
├── streamlit.py               # Streamlit frontend
└── requirements.txt           # Project dependencies
```

## How to Run the Project

1. **Clone the repository** and navigate to the project folder.
2. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate   # On Linux/Mac
   env\Scripts\activate      # On Windows
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Run FastAPI server**:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.
5. **Run Streamlit app**:

   ```bash
   streamlit run app.py
   ```

   Open the provided URL in your browser to use the application.

## Usage

* Input your personal and lifestyle details through the Streamlit interface.
* The data will be sent to the FastAPI backend for prediction.
* The predicted obesity level will be displayed on the screen.
