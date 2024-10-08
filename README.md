


# Bati Bank Credit Scoring Model
```

## Table of Contents
```
- [Overview](#overview)
- [Business Need](#business-need)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview
```
Bati Bank, a leading financial service provider with over 10 years of experience, is partnering with a successful eCommerce company to enable a buy-now-pay-later service. This project focuses on creating a Credit Scoring Model using data provided by the eCommerce platform, allowing customers to purchase products on credit based on their creditworthiness.

```
## Business Need
```

Credit scoring is essential for assessing potential borrowers and estimating the likelihood of default. This project aims to:
1. Define a proxy variable to categorize users as high risk (bad) or low risk (good).
2. Select observable features that are good predictors of default.
3. Develop a model that assigns risk probability to new customers.
4. Develop a model that assigns credit scores from risk probability estimates.
5. Develop a model that predicts the optimal amount and duration of the loan.

## Getting Started
```
To get a local copy up and running, follow these steps:

1. Clone the repo
   ```bash
   git clone https://github.com/yourusername/bati-bank-credit-scoring.git
   ```
2. Navigate to the project directory
   ```bash
   cd bati-bank-credit-scoring
   ```
3. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure
```
bati-bank-credit-scoring/
│
├── data/
│   ├── transactions_data.csv               # Original dataset
│   ├── cleaned_data.csv                    # Cleaned dataset after preprocessing
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb        # Data preprocessing
│   ├── 02_exploratory_data_analysis.ipynb  # Exploratory Data Analysis
│   ├── 03_feature_engineering.ipynb        # Feature Engineering
│   ├── 04_credit_scoring_model.ipynb       # Credit Scoring Model Development
│   └── 05_model_serving_api.ipynb          # Model serving with FastAPI
│
├── requirements.txt                         # List of required packages
├── best_model.pkl                           # Trained machine learning model
└── README.md                                # Project documentation
```

## Tasks
1. **Data Preprocessing:** Load, clean, and prepare the dataset for analysis.
2. **Exploratory Data Analysis (EDA):** Analyze the data to understand patterns and relationships.
3. **Feature Engineering:** Create and select relevant features for the credit scoring model.
4. **Model Development:** Develop models to predict risk probabilities and credit scores.
5. **Model Serving:** Create a REST API to serve the trained models for real-time predictions.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- FastAPI
- Uvicorn

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Instruction
1. Replace `yourusername` in the clone URL with your actual GitHub username.
2. Update the dataset links with the correct URLs.
3. Add more sections if needed, such as "Examples" for how to use the API.
4. Make sure to include a `requirements.txt` file listing all necessary Python packages.
```

