import streamlit as st
import requests

# Page setup for premium aesthetics
st.set_page_config(page_title="Mobile Addiction Analyzer", page_icon="📱", layout="centered")

# Custom CSS for UI Enhancement
st.markdown("""
<style>
    .main {
        background-color: #0c0f12;
        color: #f0f2f6;
    }
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #bb86fc 0%, #3700b3 100%);
    }
    div[data-testid="stMetricValue"] {
        font-size: 30px;
        color: #bb86fc;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #bb86fc 0%, #3700b3 100%);
        color: white;
        font-size: 20px;
        border-radius: 10px;
        border: none;
        padding: 10px;
        box-shadow: 0px 4px 10px rgba(187, 134, 252, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 15px rgba(187, 134, 252, 0.6);
        color: white;
        border-color: transparent;
    }
    .result-box {
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        text-align: center;
        background: rgba(187, 134, 252, 0.1);
        border: 1px solid #bb86fc;
        box-shadow: 0px 0px 20px rgba(187, 134, 252, 0.2);
    }
    .title-text {
        text-align: center;
        background: -webkit-linear-gradient(#bb86fc, #03dac6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        margin-bottom: 30px;
        font-size: 3em;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>📱 Mobile Addiction Analyzer</h1>", unsafe_allow_html=True)
st.write("Understand your digital habits and check your mobile addiction level using Machine Learning.")

with st.container():
    st.subheader("📊 Your Daily Mobile Habits")
    
    col1, col2 = st.columns(2)
    with col1:
        screen_time = st.slider("Daily Screen Time (hours)", 0.0, 24.0, 4.0, step=0.5)
        social_media = st.slider("Time on Social Media (hours)", 0.0, 24.0, 2.0, step=0.5)
        usage_before_sleep = st.slider("Usage Before Sleep (hours)", 0.0, 5.0, 1.0, step=0.25)
    with col2:
        gaming_time = st.slider("Gaming Time (hours)", 0.0, 24.0, 1.0, step=0.5)
        phone_checks = st.number_input("Phone Checks per day", min_value=0, max_value=1000, value=80, step=10)
        usage_after_waking = st.slider("Usage within waking up (minutes)", 0, 120, 15, step=5)
        
    interruption_str = st.radio("Do phone notifications interrupt your work/study?", ["No", "Yes"], horizontal=True)
    interruption = 1 if interruption_str == "Yes" else 0

if st.button("Analyze My Habits", use_container_width=True):
    # Calculate approx daily addiction time
    daily_addict_time = sum([social_media, gaming_time])
    # Prevent exceeding screen time logically
    daily_addict_time = min(daily_addict_time, screen_time)
    
    payload = {
        "screen_time": screen_time,
        "social_media": social_media,
        "phone_checks": int(phone_checks),
        "usage_before_sleep": usage_before_sleep,
        "usage_after_waking": usage_after_waking,
        "gaming_time": gaming_time,
        "interruption": interruption
    }
    
    api_url = "http://127.0.0.1:5000/predict"
    
    with st.spinner("Analyzing your habits..."):
        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                result = response.json()
                prediction = result["prediction"]
                level_index = result["level_index"]
                
                # Dynamic text and colors based on level
                if level_index == 0:
                    color = "#03dac6"
                    suggestions = "👍 Great job! You have a healthy relationship with your phone. Keep up the good work!"
                elif level_index == 1:
                    color = "#f6c342"
                    suggestions = "⚠️ You have a moderate level of attachment. Consider setting some digital boundaries, especially before sleep."
                else:
                    color = "#cf6679"
                    suggestions = "🚨 High level of mobile addiction detected! We strongly recommend setting screen time limits, doing a digital detox, and finding offline hobbies."
                
                # Progress bar visualization
                progress_val = {0: 33, 1: 66, 2: 100}[level_index]
                st.markdown(f"<p style='margin-bottom: 5px; font-weight: bold;'>Severity Level: {progress_val}%</p>", unsafe_allow_html=True)
                st.progress(progress_val)
                
                st.markdown(f"""
                <div class="result-box" style="border-color: {color}; box-shadow: 0px 0px 20px {color}40;">
                    <h2 style="color: {color};">Result: {prediction}</h2>
                    <p style="font-size: 18px;">Estimated Non-Productive Screening: <b>{daily_addict_time} hours</b>/day</p>
                    <p style="font-size: 16px; margin-top: 15px;"><i>{suggestions}</i></p>
                </div>
                """, unsafe_allow_html=True)
                
            else:
                st.error(f"API Error ({response.status_code}): {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the backend API. Please make sure the Jupyter Notebook is running and the FastAPI server is started on localhost:5000.")

st.markdown("<hr><p style='text-align: center; color: #666;'>Powered by Machine Learning • Mobile Addiction Analyzer</p>", unsafe_allow_html=True)
