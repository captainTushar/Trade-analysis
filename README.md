📊 Trade Analysis Using Market Sentiment

This project explores how market sentiment (Fear vs Greed) influences trader behavior and performance. The goal is to uncover patterns that can help design smarter, data-driven trading strategies.

This work was completed as part of a data science assignment involving behavioral analysis of traders under different market emotion regimes.

🧠 Problem Statement

Markets are driven not only by price but also by investor psychology. This project analyzes how trader behavior changes when the market is fearful versus greedy.

We combine:

Bitcoin Fear/Greed sentiment data

Historical trader execution data

We aim to answer:

Do traders perform differently during Fear vs Greed?

Do they change their risk-taking behavior?

Which trader types benefit the most?

Can we predict trader profitability using sentiment and behavioral metrics?


📂 Project Structure


Trade-analysis/
│
├── analysis.ipynb                # Full exploratory data analysis
├── app.py                        # Streamlit prediction app
├── trader_model_pipeline.pkl     # Trained ML pipeline
├── requirements.txt              # Dependencies
└── README.md                     # Documentation

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/captainTushar/Trade-analysis.git
cd Trade-analysis

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

3️⃣ Install Dependencies:
pip install -r requirements.txt

▶️ How to Run
📓 Run Data Analysis Notebook
jupyter notebook


Open:

analysis.ipynb


Run all cells to reproduce data cleaning, analysis, charts, and insights.

🌍 Run Streamlit App
streamlit run app.py


The app opens in your browser and allows users to:

Enter trader behavior metrics

Select market sentiment

Predict whether a trader is likely to be profitable



