# Satellite Imagery Based Property Valuation

# Overview
This project focuses on predicting property prices using tabular property features and satellite imagery.
A multimodal deep learning approach is implemented, where tabular data is used as the primary predictor and satellite image features are integrated to enhance model understanding.

The final output of the project is a CSV file containing predicted property prices for unseen data.

# Project Structure
project/
├── data_fetcher.py
├── preprocessing.ipynb
├── model_training.ipynb
├── enrollno_final.csv
├── data/
│ └── images/
├── notebooks/
└── README.md

# File Descriptions
- **data_fetcher.py**  
  Script to download and store satellite images for properties using latitude and longitude.

- **preprocessing.ipynb**  
  Handles data cleaning, exploratory data analysis (EDA), feature preprocessing, and target transformation.

- **model_training.ipynb**  
  Contains dataset definitions, model architectures (tabular and multimodal), training routines, evaluation metrics, and prediction generation.

- **23116036_final.csv**  
  Final prediction file in the required format: id, predicted_price.


# Tech Stack
- Python
- PyTorch
- Pandas, NumPy
- Scikit-learn
- Torchvision
- Jupyter Notebook


# How to Run the Project

This section describes the step by step process to set up the environment, run the code, and generate predictions.


# Step 1: Environment Setup


Ensure that Python (version 3.8 or higher) is installed.

Install the required dependencies using pip:

pip install torch torchvision pandas numpy scikit-learn pillow matplotlib seaborn.
If a virtual environment is used, activate it before installing the dependencies.

# Step 2: Satellite Images

run the following script:

python data_fetcher.py

This script:

Downloads satellite images using latitude and longitude information

Stores the images in the data/images/ directory

# Step 3: Data Preprocessing and EDA

Open and run the notebook: preprocessing.ipynb


This notebook performs:

Loading of the dataset

Handling missing values

Feature selection and scaling

Exploratory Data Analysis (EDA) with visualizations

Target variable transformation for stable model training

The processed data from this step is used for model training.

# Step 4: Model Training

Open and run the notebook: model_training.ipynb


This notebook includes:

Dataset definitions

Tabular regression model

Multimodal model (tabular + satellite imagery)

Model training and evaluation using RMSE and R² metrics

The tabular model is selected for final predictions due to its stable performance. 

# Step 5: Prediction Generation

Prediction Generation

At the end of model_training.ipynb, predictions are generated on unseen test data.

The notebook:

Loads the trained model

Performs inference on test data

Saves predictions to a CSV file

The output file generated is: enrollno_final.csv, The file format is strictly: id,predicted_price

 

