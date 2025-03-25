
# Real-Time AQI Prediction Dashboard  

## 📌 Project Overview  
This project is a **Real-Time Air Quality Index (AQI) Prediction Dashboard** that helps analyze, visualize, and predict air quality metrics using machine learning models. The web-based application provides real-time insights into air pollution trends and forecasts AQI levels.

## 🌟 Features  
- **Interactive AQI Dashboard**: Visualizes air pollution metrics (PM2.5, PM10, NO2, etc.) with clear, interactive charts.  
- **24-Hour AQI Forecast**: Predicts AQI levels for the next 24 hours using a trained **Gradient Boosting model**.  
- **Historical Trend Analysis**: Displays historical air quality trends and correlations with other factors, such as traffic.  
- **Feature Importance Analysis**: Highlights key factors influencing AQI predictions.  
- **Responsive Design**: Works smoothly on desktop and mobile devices.  

## 🛠️ Tech Stack  
- **Python (Flask)**: Backend framework for serving the web app.  
- **Machine Learning**: Used `GradientBoostingClassifier` for AQI prediction.  
- **Pandas & NumPy**: Data handling and preprocessing.  
- **Matplotlib & Plotly**: For interactive data visualization.  
- **HTML, CSS, JavaScript**: Frontend design and interactivity.

## 🚀 How to Run the Project Locally  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/AbdulSarban/Real-Time-AQI-Prediction.git  
   cd Real-Time-AQI-Prediction  
   ```  

2. **Set up a Virtual Environment (Optional but Recommended)**:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Run the Application**:  
   ```bash  
   python app.py  
   ```  
   The app will be running locally at `http://127.0.0.1:5000`.

## 📊 Dataset  
- **city_day.csv**: This dataset contains historical air quality data, including PM2.5, PM10, SO2, NO2, and AQI values.  
  Source: [CPCB Air Quality Data](https://www.cpcb.nic.in/)

## ⚙️ Model Information  
- The AQI prediction is powered by a trained **Gradient Boosting** model (`gradient_boosting_model.joblib`), which provides accurate AQI forecasts based on key environmental features.

## 📖 Project Structure  
```
├── app.py                            # Main Flask app  
├── city_day.csv                      # Dataset for historical air quality data  
├── finalfile.ipynb                   # Jupyter Notebook for data exploration and model training  
├── gradient_boosting_model.joblib    # Trained machine learning model  
├── README.md                         # Project documentation (this file)  
```

## 💡 Future Improvements  
- Integrate **real-time AQI API** to update live data.  
- Deploy the application on **Heroku** or **Render** for public access.  
- Implement **geolocation-based AQI** tracking.

## 🙌 Contributors  
- **Abdul Mahtab Sarban** – Project Lead & Developer  
