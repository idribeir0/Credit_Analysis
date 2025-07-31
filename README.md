# 🏦 Credit Analysis

Personal project for credit risk analysis simulation. The goal is to explore customer data and create insights for risk classification.

## 📊 About the Project

This project uses the **UCI Credit Card** dataset to perform credit risk analysis. It's an educational simulation to learn about data analysis and machine learning.

## 📁 Project Structure

```
Credit/
│
├── data/                    # Data files
│   └── UCI_Credit_Card.csv # Main dataset (30,000 records)
├── notebooks/               # Jupyter notebooks
│   ├── 01_exploration.ipynb # Initial data exploration ✅
│   ├── 02_eda.ipynb        # Exploratory data analysis ✅
│   ├── 03_preprocessing.ipynb # Data preprocessing (planned)
│   ├── 04_modeling.ipynb   # Model development (planned)
│   └── 05_results.ipynb    # Results analysis (planned)
├── src/                     # Python code
│   ├── download_data.py    # Script to download data ✅
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

## 🛠️ What's Already Implemented

### ✅ Basic Structure
- Organized project structure
- Functional data download script
- Complete Python dependencies list
- README with instructions
- Git repository setup
- UCI Credit Card dataset loaded (30,000 records, 25 columns)

### ✅ Data Exploration (01_exploration.ipynb)
- Initial data loading and visualization
- Dataset structure information
- Basic descriptive statistics
- Data dimensions verification

### ✅ Exploratory Data Analysis (02_eda.ipynb)
- **Data preprocessing**:
  - ID column removal
  - Categorical variable encoding (EDUCATION, MARRIAGE, SEX)
  - Age range creation
- **Implemented visualizations**:
  - Default distribution
  - Age range distribution
  - Default rate by gender
  - Credit limit vs default relationship
- **Statistical analysis**:
  - Correlation analysis
  - Numerical variable distributions
  - Outlier analysis

### 📊 UCI Credit Card Dataset
- **30,000 records** of customers
- **25 columns** including:
  - Demographic information (age, gender, education, marital status)
  - Payment history (PAY_0 to PAY_6)
  - Bill amounts (BILL_AMT1 to BILL_AMT6)
  - Payment amounts (PAY_AMT1 to PAY_AMT6)
  - Target variable: `default.payment.next.month`

## 📝 Next Steps

- [ ] Implement preprocessing functions in `src/preprocessing.py`
- [ ] Complete preprocessing notebook (03_preprocessing.ipynb)
- [ ] Develop machine learning models (04_modeling.ipynb)
- [ ] Analyze and present results (05_results.ipynb)
- [ ] Add unit tests
- [ ] Implement cross-validation
- [ ] Create complete modeling pipeline

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Matplotlib/Seaborn** - Visualizations
- **Plotly** - Interactive plots
- **Scikit-learn** - Machine Learning
- **XGBoost/LightGBM** - Advanced algorithms
- **Jupyter** - Interactive notebooks

---

**Note**: This is a study project. The data is fictional or public domain.