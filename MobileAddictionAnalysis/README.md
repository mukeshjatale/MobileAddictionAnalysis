# 📱 Mobile Addiction Analyzer

Welcome to the **Mobile Addiction Analyzer**, an interactive, machine learning-powered web application designed to help users understand their digital habits and evaluate their mobile addiction levels. 

By analyzing indicators like screen time, gaming habits, sleep distraction, and productivity interruptions, the system classifies phone usage behavior into levels of addiction (**Low**, **Moderate**, or **High**) and provides actionable suggestions for maintaining a healthy digital lifestyle.

---

## 🏗️ Project Architecture & Components

The application is structured into a backend API that serves the Machine Learning predictions and a frontend Streamlit dashboard for a modern, responsive user experience:

```
MobileAddictionAnalysis/
│
├── model_and_api.ipynb         # Jupyter Notebook for synthetic data generation, model training, and notebook API testing
├── teen_phone_addiction_dataset.csv # The dataset containing usage statistics and labels
├── model.pkl                   # Trained and serialized Random Forest Classifier model
├── api.py                      # Production-ready FastAPI backend server
├── app.py                      # Sleek, premium Streamlit frontend client
└── requirements.txt            # List of Python dependencies
```

---

## 🚀 Key Features

* **Machine Learning Core**: Employs a **Random Forest Classifier** trained on mobile usage patterns to deliver accurate predictions.
* **REST API Server**: Built with **FastAPI** to handle real-time prediction requests over a clean HTTP JSON interface.
* **Premium Dark Mode UI**: Custom-styled Streamlit frontend featuring interactive sliders, progress bars, hover animations, and a rich, curated color palette (violet-to-indigo gradients).
* **Personalized Analysis & Feedback**: Estimates unproductive screen time and provides tailor-made recommendations to help users build healthier habits.

---

## 📊 Parameters Analyzed

The classifier evaluates the following parameters to calculate the addiction score:

| Metric | Type | Description |
| :--- | :--- | :--- |
| **Screen Time** | `float` | Total hours spent on the phone per day |
| **Social Media Time** | `float` | Hours spent browsing social platforms (Instagram, TikTok, etc.) |
| **Phone Checks** | `int` | Approximate number of times the phone is unlocked/checked daily |
| **Usage Before Sleep** | `float` | Hours spent on the phone immediately before bedtime |
| **Usage After Waking** | `int` | Minutes until the phone is checked after waking up |
| **Gaming Time** | `float` | Hours spent playing mobile games per day |
| **Interruption** | `binary (0/1)` | Whether notifications frequently interrupt work or study |

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Clone/Open the Project Directory
Navigate to the root directory where the project files are located:
```bash
cd "d:\College work\3 rd Year\2ndSem\Project\DSBDA\MobileAddictionAnalysis"
```

### 3. Install Dependencies
Install all required libraries using `pip`:
```bash
pip install -r requirements.txt
```

*Dependencies installed include: `streamlit`, `fastapi`, `uvicorn`, `scikit-learn`, `pandas`, `requests`, `nest-asyncio`, and `jupyter`.*

---

## 🚦 How to Run the Application

To use the application, you need to run both the backend API and the frontend dashboard in separate terminal windows.

### Step 1: Start the FastAPI Backend Server
Launch the FastAPI server on port `5000` using `uvicorn`:
```bash
uvicorn api:app --host 127.0.0.1 --port 5000
```
*Note: The API server will be available at `http://127.0.0.1:5000`. You can inspect the interactive OpenAPI docs at `http://127.0.0.1:5000/docs`.*

### Step 2: Start the Streamlit Frontend Client
Open a new terminal/command prompt and start the Streamlit web interface:
```bash
streamlit run app.py
```
*The Streamlit web page will automatically launch in your default web browser (typically at `http://localhost:8501`).*

---

## 📈 Model Training Detail

The predictive model is trained using a `RandomForestClassifier` with 100 estimators.
* **Data Origin**: The model uses the features in `teen_phone_addiction_dataset.csv` generated synthetically by evaluating weighted factors.
* **Addiction Score Weights**:
  $$\text{Score} = (2 \times \text{ScreenTime}) + (3 \times \text{SocialMedia}) + \left(\frac{\text{Checks}}{20}\right) + (4 \times \text{SleepUsage}) + \left(\frac{\text{WakingUsage}}{10}\right) + (1.5 \times \text{Gaming}) + (15 \times \text{Interruption})$$
* **Thresholds**:
  * **Low**: Score $< 35$
  * **Moderate**: $35 \le$ Score $< 60$
  * **High**: Score $\ge 60$
