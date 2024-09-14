[![Python Application Test with Github Actions - Pandas Project Su Zhang](https://github.com/nogibjj/Su_Zhang_Pandas_Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Su_Zhang_Pandas_Project/actions/workflows/cicd.yml)

# Su Zhang Pandas Project - IDS706 Week 2 Assignment
This project aims to analyze a dataset on patients' healthcare records, which includes patient age, gender, blood type, medical condition, billing amount, medication etc. Please note that these data are not real-world data and are just for descriptive data practice. This project primarily used Pandas and Matplotlib packages to analyze the distribution of billing amount, summary statistics (mean, median, max, standard variation) of billing amount, and age. This project also showcased the distribution of subcategories in tables for the categorical variables, such as blood type, medical condition, admission type, and test results. 

# Source of data: 
https://www.kaggle.com/datasets/prasad22/healthcare-dataset/data

# Project Structure
- Makefile: Build automation commands: in this project, commands mainly include install, format, lint, and test.
- requirements.txt: Specify Python dependencies needed for this project and for this project, added packages of pandas and matplotlib.
- main.py: Main application script to read the input data and create functions to print out first few rows of dataset, summarize the key statistics, build histogram for specific data category
- test_main.py: Tests if the functions defined in main.py work normally
- README.me: Project documentation to offer an overview of the project
- github actions: Describes the steps and jobs that GitHub should run automatically. In this project, this includes installing dependencies and packages, lint, format, and test.
- devcontainer: Set up a development environment in Github Codespace, and Dockerfile to define the base environment (such as what tools and libraries are installed)
- healthcare_dataset.csv: Input dataset on patients healthcare records
- Billing_Amount_Hist.png: Output histogram graph demonstrating the distribution of billing amount
- Data_Summary.pdf: Output pdf generated from Jupyter Notebook to showcase the analysis output

# Summary Statistics of Age and Billing Amount
<img width="290" alt="Screen Shot 2024-09-14 at 3 56 21 PM" src="https://github.com/user-attachments/assets/c2d73b76-8a65-4a0b-861b-9d559c85cf9e">

# Histogram of Billing Amount Distribution
![Graph Description](./Billing_Amount_Hist.png)

