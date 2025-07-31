# 🏦 Credit Analysis

Personal project for credit risk analysis simulation. The goal is to explore customer data and create insights for risk classification.

## 📊 About the Project

This project uses the **UCI Credit Card** dataset to perform credit risk analysis. It's an educational simulation to learn about data analysis and machine learning.

## 📁 Project Structure

```
Credit/
│
├── data/                    # Data files
│   └── UCI_Credit_Card.csv # Main dataset
├── notebooks/               # Jupyter notebooks
│   ├── 01_exploration.ipynb # Initial data exploration
│   ├── 02_eda.ipynb        # Exploratory data analysis
│   ├── 03_preprocessing.ipynb # Data preprocessing (planned)
│   ├── 04_modeling.ipynb   # Model development (planned)
│   └── 05_results.ipynb    # Results analysis (planned)
├── src/                     # Python code
│   ├── download_data.py    # Script to download data
│   └── preprocessing.py    # Data preprocessing functions (empty)
├── tests/                   # Tests (future)
├── README.md               # This file
├── requirements.txt        # Python dependencies
└── .gitignore             # Git ignore file
```

## 🚀 How to Use

1. **Clone the project** (when on GitHub)
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the download script**:
   ```bash
   python src/download_data.py
   ```
4. **Open notebooks**:
   ```bash
   jupyter notebook notebooks/
   ```

## 🛠️ What's Already Done

- ✅ Basic project structure
- ✅ Data download script
- ✅ Python dependencies list
- ✅ README with instructions
- ✅ Git repository setup
- ✅ Data exploration notebooks (01_exploration.ipynb, 02_eda.ipynb)
- ✅ UCI Credit Card dataset loaded

## 📝 Next Steps

- [ ] Complete data preprocessing functions
- [ ] Finish preprocessing notebook (03_preprocessing.ipynb)
- [ ] Develop machine learning models (04_modeling.ipynb)
- [ ] Analyze and present results (05_results.ipynb)
- [ ] Add unit tests

---

**Note**: This is a study project. The data is fictional or public domain.